import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from langgraph.checkpoint.memory import InMemorySaver

from api.db import get_session
from api.ai.agents import get_supervisor
from api.ai.schemas import EmailMessageSchema, SupervisorMessageSchema
from api.ai.services import generate_email_message
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem

router= APIRouter()
checkpointer = InMemorySaver()


@router.get("/")
def chat_check():
    return {"status" : "ok"}


@router.get("/recent", response_model= List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results= session.exec(query).fetchall()[:10]
    return results



@router.post("/", response_model=SupervisorMessageSchema)
def chat_create_message(
    payload:ChatMessagePayload,
    session: Session = Depends(get_session)
    ):
    data = payload.model_dump() # pydantic -> dict
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    thread_id = uuid.uuid4()
    supe = get_supervisor(checkpointer=checkpointer)
    msg_data = {
        "messages": [
            {"role": "user",
            "content": f"{payload.message}" 
          },
        ]
    }
    result = supe.invoke(msg_data, {"configurable": {"thread_id": thread_id}})
    if not result:
        raise HTTPException(status_code=400, detail="Error with supervisor")
    messages = result.get("messages")
    if not messages:
        raise HTTPException(status_code=400, detail="Error with supervisor")
    return messages[-1]

    return response