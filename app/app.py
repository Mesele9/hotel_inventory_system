import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from db import engine

load_dotenv('.env')


db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{}:{}@{}/{}".format(
    db_username, db_password, db_host, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

#db.init_app(app)
db = SQLAlchemy(app)

from models import *
# # Set up the database connection
# with app.app_context():
#     db.create_all()

@app.route('/')
def index():   
    # with app.app_context:
    #     inspector = db.ispect(db.engine)
    #     table_names = inspector.get_table_names()
    #     return table_names
    return redirect(url_for('login'))



@app.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('login.html')

@app.route('/table')
def show_table():
    inspector = db.inspect(engine)
    table_names = inspector.get_table_names()
    return table_names


@app.route('/add_user', methods=['GET','POST'])
def add_user():
#    return render_template('add_user.html')
    if request.method == 'POST':
        # get the data from form
        name = request.form["name"]
        username = request.form["username"] 
        password = request.form["password"]
        role = request.form["role"]

        # create the user
        new_user = User(name=name, username=username, password=password, role=role)   
    
        # add the user to the session
        db.session.add(new_user)

        # commit the session
        db.session.commit()

        
        return redirect(url_for('login'))
    
    return render_template('add_user.html')

    
@app.route('/users')
def user_list():
    users = db.session.execute(db.select(User)).scalars()
    user=[]
    for u in users:
        user.append(u.name)
    return user





if __name__ == "__main__":
    app.run(debug=True)