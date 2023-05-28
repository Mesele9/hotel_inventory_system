from flask import Blueprint


bp = Blueprint('issue', __name__)

from app.manage_issue_bp import routes
