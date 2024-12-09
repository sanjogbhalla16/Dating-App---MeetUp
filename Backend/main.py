#At last we make changes in the main file
#Add the db here
from typing import Union
from fastapi import FastAPI
from  .routes import routes
from .database import db

# Initialize FastAPI app
app = FastAPI()

# Include routes
app.include_router(routes.router,prefix="/auth")

# Database connection events
@app.on_event("startup")
async def startup_event():
    # Initialize database connection
    print("Connecting to the database...")
    await db.connect()


@app.on_event("shutdown")
async def shutdown_event():
    # Close database connection
    print("Disconnecting from the database...")
    await db.disconnect()
    
# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Dating App!"}