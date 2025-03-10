import os
import uuid
from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, Field, create_engine

class User(SQLModel,table=True):
    id: uuid.UUID = Field(primary_key=True,default_factory=uuid.uuid4)
    username:str = Field(nullable=False, index=True)
    password:str = Field(nullable=False, index=True)

load_dotenv()
database_username:str = os.getenv("DB_USER_NAME")
database_password:str = os.getenv("PASSWORD")
database_host:str = os.getenv("HOST") 
database_port:str = os.getenv("PORT")
database_name: str = os.getenv("DB_NAME")
database_url:str = f"postgresql+psycopg://{database_username}:{database_password}@{database_host}:{database_port}/{database_name}"

engine = create_engine(url=database_url,echo=True)


def create_database():
    SQLModel.metadata.create_all(engine)

create_database()
#add_data()


    
