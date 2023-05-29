from flask import Blueprint
from flask import render_template, url_for, redirect, request
from app.dbcon import db

product_bp = Blueprint('product_bp', __name__, url_prefix='/products')


@product_bp.route('/')
def index():
    
    return ''"<h1>This is from Product Blueprint</h1>"

