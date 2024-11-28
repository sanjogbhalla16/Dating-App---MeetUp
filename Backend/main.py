#At last we make changes in the main file
#Add the db here
from typing import Union
from fastapi import FastAPI
from Backend import config
from .routes import auth
from Backend.database import db

# Initialize FastAPI app
app = FastAPI(
    title="Dating App",
    description="A dating app backend built with FastAPI, Prisma, and PostgreSQL.",
    version="1.0.0",
)


# Include routes
app.include_router(auth.router,prefix="/auth")

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