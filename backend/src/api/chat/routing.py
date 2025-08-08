from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.db import get_session

router= APIRouter()


@router.get("/")
def chat_check():
    return {"status" : "ok"}


@router.get("/recent", response_model= List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results= session.exec(query).fetchall()[:10]
    return results



@router.post("/", response_model=ChatMessage)
def chat_create_message(payload: ChatMessagePayload, session: Session = Depends(get_session)):
    data= payload.model_dump()
    print(data)
    obj_instance = ChatMessage.model_validate(data)
    session.add(obj_instance)
    session.commit()
    session.refresh(obj_instance)

    return obj_instance