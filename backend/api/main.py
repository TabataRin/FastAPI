from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN

from pydantic import BaseModel

from databases import Database
from typing import List

DATABASE_URL = "postgresql://root:secret@postgres:5432/mydb"
database = Database(DATABASE_URL)

from routers import test
from util import util

class Message(BaseModel):
    message: str

class Contact(BaseModel):
    id: int
    name: str
    phone_number: str

correct_key: str = util.get_apikey()
api_key_header = APIKeyHeader(name='Authorization', auto_error=False)

async def get_api_key(
    api_key_header: str = Security(api_key_header),
    ):
    if api_key_header == correct_key:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )

app = FastAPI()
app.include_router(test.router, dependencies=[Depends(get_api_key)], tags=["ユーザー情報"])

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.post("/echo")
def return_echo(message:Message):
    return {"content":message.message}

@app.get("/hoge")
def read_hoge():
    hoge = open('hoge.txt',"r")
    content = hoge.read()
    return {"content":content}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/contact/", response_model=List[Contact])
async def read_user():
    query = "SELECT * FROM contacts"
    return await database.fetch_all(query=query)