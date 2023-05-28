from flask import Blueprint


bp = Blueprint('product', __name__)

from app.manage_product_bp import routes
