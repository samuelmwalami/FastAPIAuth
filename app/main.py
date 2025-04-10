from datetime import timedelta
from typing import Annotated
from fastapi import FastAPI, status, Form ,Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app.database.database_service import DatabaseService
from app.database.database_models import User
from app.utils import hashing_util
from app.utils.jwt_util import JWTUtil
from app.form_models import  AuthForm
from app.config import DataBaseConfig, JwtConfig

app = FastAPI()

OAuth2Scheme = OAuth2PasswordBearer(tokenUrl="login")

def authenticate_user(username:str,password:str) ->dict:
    conn = DatabaseService(DataBaseConfig().database_url)
    user:User = conn.get_user_by_name(username)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials no user")
        
    if not hashing_util.verify_password(password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials pwd")
    
    payload ={
    "sub" : user.user_name
    }
    token_context = JWTUtil(JwtConfig().get_algorithm(),JwtConfig().get_secret(),timedelta(minutes=5))
    token = token_context.get_jwt_from_string(payload)
    return  {
        "User Name" : user.user_name,
        "Token" : token,
        }
        

    

@app.post("/signup", status_code=status.HTTP_201_CREATED)
def sign_up(signup_form: Annotated[AuthForm, Form()]):
    user_name:str = signup_form.username
    password:str = hashing_util.hash_password(signup_form.password)
    conn = DatabaseService(DataBaseConfig().database_url)
    user = conn.create_user(user_name=user_name,password=password)
    
    return user

@app.post("/login", status_code=status.HTTP_201_CREATED)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    username:str = form_data.username
    password:str = form_data.password
    user = authenticate_user(username, password)
    return user
    
