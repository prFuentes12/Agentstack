from fastapi import FastAPI
import os

app = FastAPI()

API_KEY= os.environ.get("API_KEY")

@app.get("/")
def get_index():
    return {"hello" : API_KEY}