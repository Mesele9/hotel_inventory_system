from flask import render_template, url_for, redirect, request
from app.manage_product_bp import bp
from app.dbcon import db
#from app.models import *


@bp.route('/')
def index():
    
    return ''"<h1>This is from Product Blueprint</h1>"

