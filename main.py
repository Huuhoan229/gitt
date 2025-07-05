from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

class Message(BaseModel):
    prompt: str

@app.post("/chat")
def chat(data: Message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": data.prompt}]
    )
    return {"reply": response.choices[0].message["content"]}
