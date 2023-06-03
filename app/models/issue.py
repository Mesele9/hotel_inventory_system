from datetime import datetime
from app.dbcon import db


# define a junction class between issue order product table
class ProductIssueOrder(db.Model):
    __tablename__ = 'product_issue_order'

    issue_order_id = db.Column(db.Integer, db.ForeignKey('issue_order.id'), primary_key=True)
    products_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Integer)


    def __repr__(self):
        return '<ProductIssueOrder (IssueOrder={}, Product={}, Quantity={})>'.format(
                self.issue_order_id, self.products_id, self.quantity)


# define issueorder model
class IssueOrder(db.Model):
    __tablename__ = 'issue_order'

    id = db.Column(db.Integer, primary_key=True)
    requested_date = db.Column(db.Date, nullable=False, default=datetime.now().date())
    requested_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(20), default='Requested')


    users = db.relationship("Users", backref="issue_order")
    products_issue = db.relationship('ProductIssueOrder', backref='issue_order', lazy='dynamic', cascade='all, delete')

    
    def __repr__(self):
        return '<Issue Order: {} {} : {}>'.format(self.id, self.requested_by, self.status)
    
