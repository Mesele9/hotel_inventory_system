from flask import Blueprint


bp = Blueprint('purchase', __name__)

from app.manage_purchase_bp import routes
