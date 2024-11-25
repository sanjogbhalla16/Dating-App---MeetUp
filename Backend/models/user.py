from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    
class UserProfile(BaseModel):
    email: EmailStr
    fullName: str
    profileImg: str = None
    about: str = None
    preferences: dict = None
    
