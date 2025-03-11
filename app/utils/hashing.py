from passlib.context import CryptContext

password_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str) -> str:
    return password_context.hash(password)

def verify_password(password:str,hashed_password:str) -> str:
    return password_context.verify(password,hashed_password)