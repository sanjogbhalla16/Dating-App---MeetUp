from pydantic import BaseModel,EmailStr, constr

class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    
class SigninResponse(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str    
    

class MessageCreate(BaseModel):
     content: str
     receiver_id: int
     
     
class MessageResponse(BaseModel):
    id: int
    content: str
    sender_id: int  
    receiver_id: int
    
