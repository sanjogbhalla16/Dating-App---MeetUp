#here we write the routes 
from fastapi import APIRouter,HTTPException
from ..utils.hashing import hash_password, verify_password
from ..database import db
from ..models.user import UserCreate


router = APIRouter()

@router.post("/signup")
def signup(user:UserCreate):
    pass


#for the first time signin
@router.post("/signin")
async def signin(email: str, password: str):
    #first find the user in db
    user = await db.user.find_unique(where={"email": email})
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="User already exists")
    token = create_access_token({"user_id":user.id})
    return {"access_token": token, "token_type": "bearer"}

