#here we write the routes 
from fastapi import APIRouter,HTTPException
from ..utils.hashing import hash_password, verify_password
from ..database import db
from ..models.user import UserCreate
from ..utils.auth import create_access_token


router = APIRouter()

@router.post("/signup")
async def signup(user:UserCreate):
    existing_user = db.user.find_unique({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = hash_password(user.password)
    #add the new user to db
    new_user = await db.user.create({"email":user.email,"password":hashed_password,"name":user.name})
    return {"message":"User created successfully"}


#for the first time signin
@router.post("/signin")
async def signin(email: str, password: str):
    #first find the user in db
    user = await db.user.find_unique(where={"email": email})
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="User already exists")
    token = create_access_token({"user_id":user.id})
    return {"access_token": token, "token_type": "bearer"}





