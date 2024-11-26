# we a centralized file for loading and managing configuration settings. This ensures your app doesn't repeatedly load the .env file in multiple places.

#from dotenv import load_dotenv

#load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

from dotenv import load_dotenv
import os

load_dotenv()
# Fetch environment variables
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
REFRESH_TOKEN_EXPIRE_MINUTES = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES", 10080))