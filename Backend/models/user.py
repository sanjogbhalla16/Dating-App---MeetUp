from pydantic import BaseModel,EmailStr, constr

class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr

class UserInDB(UserResponse):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str    
    
