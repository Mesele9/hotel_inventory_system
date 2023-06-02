from datetime import datetime
from app.dbcon import db


# define a junction table between issue order product table
product_issue_order = db.Table('product_issue_order',
                                  db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
                                  db.Column('issue_order_id', db.Integer, db.ForeignKey('issue_order.id'), primary_key=True),
                                  db.Column('quantity', db.Integer, nullable=False) 
)


# define issueorder model
class IssueOrder(db.Model):
    __tablename__ = 'issue_order'

    id = db.Column(db.Integer, primary_key=True)
    requested_date = db.Column(db.Date, nullable=False, default=datetime.now().date())
    requested_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(20), default='REQUESTED')

    
    users = db.relationship("Users", backref="issues_order")
    products = db.relationship('Products', secondary=product_issue_order, backref=db.backref('issue_order', lazy='dynamic'),
                               cascade='all, delete-orphan')

