from fastapi import APIRouter
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
load_dotenv()
import os

chatgpt_router = APIRouter()
openai.api_key = os.getenv('OPENAI_API_KEY')


class Input(BaseModel):
    message: str

@chatgpt_router.post("/chat")
def question(message: Input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message.message},
        ],
    )
    return {"answer": response.choices[0]["message"]["content"].strip()}
