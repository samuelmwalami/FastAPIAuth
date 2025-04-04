import os
import sys
from dotenv import load_dotenv

from .database_service import DatabaseService
from app.utils.hashing import hash_password

load_dotenv()
database_username: str = os.getenv("DB_USER_NAME")
database_password: str = os.getenv("PASSWORD")
database_host:str = os.getenv("HOST") 
database_port:str = os.getenv("PORT")
database_name: str = os.getenv("DB_NAME")

"postgresql+psycopg://username:password@host:port/db_name"
database_url:str = f"postgresql+psycopg://{database_username}:{database_password}@{database_host}:{database_port}/{database_name}"

conn = DatabaseService(database_url)
#conn.create_database()
#conn.create_user("John",hash_password("1234"))
print(conn.get_user(user_name="John",password="1234"))


