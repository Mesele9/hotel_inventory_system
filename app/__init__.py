import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Set up the database connection


@app.route('/')
def index():
    return 'Hello Mesele'

if __name__ == "__main__":
    app.run(debug=True)