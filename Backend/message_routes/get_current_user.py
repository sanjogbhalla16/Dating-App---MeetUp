from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from models import User
from database import db
from ..data_config import JWT_SECRET_KEY, ALGORITHM


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
        Validates the JWT token and retrieves the user from the database.
    """
    try:
        #decode the JWT token
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email")    
    
    #retrieve the user from the database
    user = await db.user.find_unique(where={"email": email})
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    return user
    
    