import os
from dotenv import load_dotenv

class DataBaseConfig:
    def __init__(self):
        load_dotenv()
        self.database_user_name = os.getenv("DB_USER_NAME")
        self.database_password = os.getenv("DB_PASSWORD")
        self.database_host = os.getenv("DB_HOST")
        self.database_port = os.getenv("DB_PORT")
        self.database_name = os.getenv("DB_NAME")
        self.database_url = f"postgresql+psycopg://{self.database_user_name}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_name}"
        
bss = DataBaseConfig()
print(bss.database_url)        