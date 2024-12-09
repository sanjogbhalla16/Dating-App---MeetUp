#now we write the JWT here
from datetime import datetime, timedelta
from jose import jwt
from ..data_config import JWT_SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM

def create_access_token(email:str)->str:
    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)
    
    



    
    
    
    
    
    
    
    
    
    
    
    