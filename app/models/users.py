from app.dbcon import db
from flask_login import UserMixin



# define the user model
class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<User (Name: {}, Username: {}) Role: {}'.format(self.name, self.username, self.role)
    
