import uuid
from sqlmodel import SQLModel, Field

class User(SQLModel,table=True):
    id: uuid.UUID = Field(primary_key=True,default_factory=uuid.uuid4, unique_items=True)
    user_name: str = Field(nullable=False, index=True)
    password: str = Field(nullable=False, index=True)




