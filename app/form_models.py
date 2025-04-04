from pydantic import BaseModel, Field

class AuthForm(BaseModel):
    username: str
    password:str
    model_config = {"extra":"forbid"}