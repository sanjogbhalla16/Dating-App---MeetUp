# Description: This file contains the functions related to creating a JWT token
from datetime import datetime, timedelta
from jose import jwt
from ..data_config import JWT_SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM

def create_access_token(email: str) -> str:
    """
    Create a JWT access token for the given email.

    Args:
        email (str): The email of the user for whom the token is created.

    Returns:
        str: The encoded JWT access token.
    """
    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        # You can add more claims here if needed
    }
    
    # Encode the payload using the secret key and algorithm
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)
    
    return token
    
    



    
    
    
    
    
    
    
    
    
    
    
    