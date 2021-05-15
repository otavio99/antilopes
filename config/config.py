import os
import sys
from os.path import join, dirname
from dotenv import load_dotenv

ROOT = os.getcwd()

dotenv_path = join(ROOT+'/.env')
load_dotenv(dotenv_path)

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

SECRET_KEY = os.getenv('SECRET_KEY')
EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
