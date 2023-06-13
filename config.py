import os
from dotenv import load_dotenv

load_dotenv()

db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')

# Configuration for Flask app
class Config:
    SECRET_KEY = os.urandom(16).hex()
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(db_username, db_password, db_host, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
