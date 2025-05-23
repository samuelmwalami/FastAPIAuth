from datetime import timedelta, datetime
from jose import jwt, JWTError

class JWTUtil:
    def __init__(self,algorithm: str, secret: str, expires_delta: timedelta=timedelta(minutes=30)):
        self.algorithm: str = algorithm
        self.secret:str = secret
        self.expires_delta = expires_delta
    
    def get_jwt_from_string(self, payload:dict) -> str:
        updated_payload = payload.copy()
        updated_payload = updated_payload.update({"exp":self.expires_delta,
                                                  "iat": datetime.now()})
        to_encode = jwt.encode(claims=payload, key=self.secret,algorithm=self.algorithm)
        return to_encode
    
    def get_string_from_jwt(self,jwt_token:str,error=None) -> str:
        try:
            to_decode = jwt.decode(token=jwt_token, key=self.secret)
            return to_decode
        except JWTError:
            if error:
                raise error
            else:
                print("JWT Error occurred")