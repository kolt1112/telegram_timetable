from os import environ
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = environ.get("TOKEN")
