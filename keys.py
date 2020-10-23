import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY             = os.environ.get("CONSUMER_KEY")
API_SECRET_KEY      = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN        = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
