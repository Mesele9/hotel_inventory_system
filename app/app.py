import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .db import engine

load_dotenv('.env')


db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{}:{}@{}/{}".format(
    db_username, db_password, db_host, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy()
db.init_app(app)
#db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import *


@app.route('/')
def index():   
    # with app.app_context:
    #     inspector = db.ispect(db.engine)
    #     table_names = inspector.get_table_names()
    #     return table_names
    return render_template('base.html')



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
        error = False
        try:
            name = request.form["name"]
            username = request.form["username"] 
            password = request.form["password"]
            role = request.form["role"]
      
      
            # create the user
            new_user = Users(name=name, username=username, password=password, role=role)   
    
            # add the user to the session
            db.session.add(new_user)

            # commit the session
            db.session.commit()
        except ValueError:
            error = True
            return render_template('add_user.html', error=error)
    

        
        return redirect(url_for('login'))
    
    return render_template('add_user.html')

    
@app.route('/users')
def user_list():
    result = db.session.execute(db.select(Users)).scalars()
    users_list = []
    for u in result:
        users_list.append(u.username)
    return users_list


@app.route('/delete_user/<int:id>', methods=['GET', 'POST'])
def delete_user(id):
    user = db.session.query(Users).filter_by(id=id).first()
    #request.method == 'POST':
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('add_user'))



@app.route('/add_product', methods=['GET','POST'])
def add_product():
#    return render_template('add_user.html')
    if request.method == 'POST':
        error = False
        try:
            name = request.form["name"]
            category = request.form["category"] 
            quantity = request.form["quantity"]
            unit_price = request.form["unit_price"]
      
      
            # create the user
            new_product = Product(name=name, category=category, quantity=quantity, unit_price=unit_price)   
    
            # add the user to the session
            db.session.add(new_product)

            # commit the session
            db.session.commit()
        except ValueError:
            error = True
            return render_template('add_product.html', error=error)
    

        
        return redirect(url_for('add_product'))
    
    return render_template('add_product.html')




if __name__ == "__main__":
    app.run(debug=True)
