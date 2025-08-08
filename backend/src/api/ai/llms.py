import os
from langchain_openai import ChatOpenAI


OPENAI_BASE_URL= os.environ.get("OPENAI_BASE_URL") or None
OPENAI_MODEL_NAME= os.environ.get("OPENAI_MODEL_NAME") or "gpt-4o-mini"
OPENAI_API_KEY= os.environ.get("OPENAI_API_KEY")
if OPENAI_API_KEY == "":
    raise NotImplementedError ("OPENAI ApiKey not found")


def get_openai_llm():
    open_ai_params = {
    "model" : OPENAI_MODEL_NAME,
    "api_key" : OPENAI_API_KEY,
    }
    if OPENAI_BASE_URL:
        open_ai_params["base_url"] = OPENAI_BASE_URL
    return ChatOpenAI(**open_ai_params)



