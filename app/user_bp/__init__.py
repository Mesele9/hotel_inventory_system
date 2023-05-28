from flask import Blueprint
from app.user_bp import form


bp = Blueprint('users', __name__, url_prefix='/users')

from app.user_bp import routes
#from app.user_bp import form

