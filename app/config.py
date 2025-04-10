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
        self.database_url = f"postgresql://{self.database_user_name}:{self.database_password}@{self.database_host}:{self.database_port}/{self.database_name}"
    
    # def get_database_url(self):
    #     return self.database_url
    
print(DataBaseConfig().database_url)
class JwtConfig:
    def __init__(self):
        load_dotenv()
        self.algorithm = os.getenv("ALGORITHM")
        self.secret = os.getenv("SECRET")
    
    def get_algorithm(self):
        return self.algorithm
    def get_secret(self):
        return self.secret