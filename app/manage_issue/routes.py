from flask import Blueprint
from flask import render_template, url_for, request, redirect
from app.dbcon import db


issue_bp = Blueprint('issue_bp', __name__, url_prefix='/issue')


@issue_bp.route('/')
def index():
   
    return "<h1>This is from Issue Blueprint</h1>"
    #return render_template(url_for('user.html'))

