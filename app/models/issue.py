from datetime import datetime
from app.dbcon import db


# define issueorder model
class IssueOrder(db.Model):
    __tablename__ = 'issue_order'

    id = db.Column(db.Integer, primary_key=True)
    requested_date = db.Column(db.Date, nullable=False, default=datetime.now().date())
    requested_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(20), default='REQUESTED')


    users = db.relationship("Users", backref="issue_order")
    products = db.relationship('ProductIssueOrder', backref='issue_order')
