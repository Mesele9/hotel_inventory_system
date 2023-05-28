from flask import render_template, url_for, request, redirect
from app.manage_issue_bp import bp
from app.dbcon import db
#from app.models import *


@bp.route('/')
def index():
   
    return "<h1>This is from Issue Blueprint</h1>"
    #return render_template(url_for('user.html'))

