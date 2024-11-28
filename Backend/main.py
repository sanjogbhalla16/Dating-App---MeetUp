#At last we make changes in the main file
#Add the db here
from typing import Union
from fastapi import FastAPI
from Backend import config
from .routes import auth
from Backend import db

# Initialize FastAPI app
app = FastAPI(
    title="Dating App",
    description="A dating app backend built with FastAPI, Prisma, and PostgreSQL.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}