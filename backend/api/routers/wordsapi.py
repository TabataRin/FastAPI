from fastapi import APIRouter
from pydantic import BaseModel
import requests
from dotenv import load_dotenv
load_dotenv()
import os

words_router = APIRouter()

class Input(BaseModel):
    word: str

@words_router.post("/words")
def show(input: Input):
    headers = {
        "X-RapidAPI-Key": os.getenv('RAPIDAPI_KEY'),
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }
    url_definition = f"https://wordsapiv1.p.rapidapi.com/words/{input.word}/definitions"
    url_synonyms = f"https://wordsapiv1.p.rapidapi.com/words/{input.word}/synonyms"
    response_definition = requests.get(url_definition, headers=headers)
    response_synonyms = requests.get(url_synonyms, headers=headers)

    return {
        "definitions": response_definition.json(),
        "synonyms": response_synonyms.json()
    }