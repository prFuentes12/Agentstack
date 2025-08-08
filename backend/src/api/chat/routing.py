from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.ai.services import generate_email_message
from api.db import get_session
from api.ai.schemas import EmailMessageSchema

router= APIRouter()


@router.get("/")
def chat_check():
    return {"status" : "ok"}


@router.get("/recent", response_model= List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results= session.exec(query).fetchall()[:10]
    return results



@router.post("/", response_model=EmailMessageSchema)
def chat_create_message(payload: ChatMessagePayload, session: Session = Depends(get_session)):
    data= payload.model_dump()
    print(data)
    obj_instance = ChatMessage.model_validate(data)
    session.add(obj_instance)
    session.commit()
    #session.refresh(obj_instance)

    response = generate_email_message(payload.message)
    return response