from typing import Any
from .database_models import User
from sqlmodel import SQLModel, Session, create_engine, select, col


class DatabaseService:
    def __init__(self,database_url) -> None:
        self.database_engine = create_engine(database_url,echo=True)
        
    @staticmethod
    def initialize_session(engine):
        with Session(engine) as session:
            yield session
        
    def create_database(self) -> None :
        SQLModel.metadata.create_all(self.database_engine)
        
    def create_user(self, user_name, password) -> User :
        session: Session = next(DatabaseService.initialize_session(self.database_engine))
        user: User = User(user_name=user_name,password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
        print(f"{User.user_name}\n{User.password}")
        return user
    
    def get_user(self, user_name:str, password:str) -> Any:
        session : Session = next(DatabaseService.initialize_session(self.database_engine))
        user = session.exec(select(User).where(col(User.user_name) == user_name).where(col(User.user_name)==user_name)).one()
        return user
        
