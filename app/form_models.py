from pydantic import BaseModel

class AuthForm(BaseModel):
    username: str
    password:str
    model_config = {"extra":"forbid"}