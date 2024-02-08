from flask import Flask
from dotenv import load_dotenv
import os
from pathlib import Path
d = Path(__file__).resolve().parents[1]

load_dotenv(rf"{d}/.env")
app = Flask(__name__)


def create_db_client():
    database_password = os.environ.get("DB_PASSWORD")
    database_username = os.environ.get("DB_USERNAME")
    database_server = os.environ.get("DB_SERVER")
    print(database_username)
    print(database_password)
    print(database_server)
    return None


db_client = create_db_client()

from app import routes
