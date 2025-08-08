from fastapi import FastAPI
import os
from contextlib import asynccontextmanager
from api.db import init_db
from api.chat.routing import router as chat_router
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chat")

API_KEY= os.environ.get("API_KEY")

@app.get("/")
def get_index():
    return {"hello" : API_KEY}