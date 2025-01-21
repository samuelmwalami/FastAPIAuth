from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

oauth_2 = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

@app.get("/home")
async def home(token: Annotated[str, Depends(oauth_2)]) -> dict:
    return {"message": "SUCCESSFUL",
            "token" : token,}