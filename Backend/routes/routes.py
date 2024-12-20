#here we write the routes 
from fastapi import APIRouter,HTTPException,Depends
from ..Auth_Hash.hashing import hash_password, verify_password
from ..database import db
from ..models.models import UserCreate , SigninResponse
from ..Auth_Hash.auth import create_access_token
from ..message_routes.get_current_user import get_current_user



router = APIRouter()

#User Creation for the first time
@router.post("/signup")
async def signup(user: UserCreate):
    existing_user = await db.user.find_unique(where={"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_password = hash_password(user.password)
    
    # Add the new user to db
    new_user = await db.user.create(data={
        "email": user.email,
        "password": hashed_password
    })
    
    return {"message": "User created successfully", "user_info": new_user}



#User Existing and Authentication of the user
@router.post("/signin")
async def signin(signin_request:SigninResponse):
    email = signin_request.email
    password = signin_request.password
    #first find the user in db       
    user = await db.user.find_unique(where={"email": email})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    #we will get the token for the already existing user
    token = create_access_token(email)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/message/send")
async def send_message(receiver_id:int , content:str,user=Depends(get_current_user)):
    """
    Endpoint for sending a message to another user.
    Saves the message in the database.
    """
    message = await db.message.create(data={
        "content": content, 
        "senderId": user.id, 
        "receiverId": receiver_id})
    return {"message": "Message sent successfully", "message": message} 


@router.get("/message/history")
async def get_message(receiver_id:int,user=Depends(get_current_user)):
    #gets the message between the two users
    """
    Endpoint to fetch chat history with another user.
    Retrieves messages sent and received by the authenticated user.
    """
    messages = await db.message.find_many(
        where={
            "OR": [
                {"senderId": user.id, "receiverId": receiver_id},
                {"receiverId": user.id, "receiverId": user.id}
            ]   
        },
        orderBy={"createdAt": "asc"}
    )
    return messages



