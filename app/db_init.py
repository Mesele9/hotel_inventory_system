import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# load environment variable from the .env file
load_dotenv('.env')

db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ('DB_HOST')
db_name = os.environ('DB_NAME')


# Create the database engine
db_url = 'postgresql://{}:{}@{}/{}'.format(db_username, db_password, db_host, db_name)
engine = create_engine(db_url)


# create all the tables
Base.metadata.create_all(engine)


# create a session factory
Session  = sessionmaker(bind=engine)


# create a session instance
session = Session()


# use the session to perform database operations
# ...


# close the session 
session.close()