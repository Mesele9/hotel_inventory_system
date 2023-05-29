
from flask import Blueprint
from flask import render_template, url_for, request, redirect
from app.dbcon import db
from flask_login import login_required

purchase_bp = Blueprint('purchase_bp', __name__, url_prefix='/purchase')


@purchase_bp.route('/')
@login_required
def index():
    
    return "<h1>This is from Purchase Blueprint</h1>"
    #return render_template(url_for('user.html'))

