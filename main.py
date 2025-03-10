from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

oauth_2 = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    name: str
    password: str
    age: int

fake_db = [
    {"name" : "John Doe",
     "password" : "password",
     "age" : 20,},
    {"name" : "Jane Doe",
     "password" : "password",
     "age" : 29,},
]

async def decode_token(token):
    pass
    
async def get_user(token: Annotated[str, Depends(oauth_2)]):
    pass

app = FastAPI()

@app.get("/home")
async def home(token: Annotated[str, Depends(get_user)]) -> dict:
    return {"message": "SUCCESSFUL",
            "token" : token,}