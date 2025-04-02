from typing import Annotated
from fastapi import FastAPI, status, Form ,Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app.database.database_service import DatabaseService
from app.form_models import  AuthForm

app = FastAPI()

OAuth2Scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get("/",status_code=status.HTTP_200_OK)
async def home():
    return {
    "sub" : "John Doe",
    "age" : "20",
}

@app.post("/signup", status_code=status.HTTP_201_CREATED)
def sign_up(signup_form: Annotated[AuthForm, Form()]):
    user_name = signup_form.username
    password = signup_form.password
    
    return {"username" : user_name,
            "password" : password}

@app.post("/login", status_code=status.HTTP_201_CREATED)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    username:str = form_data.username
    password:str = form_data.password
    return{"username" : username,
           "password" : password}
    
