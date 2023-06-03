""" from app.dbcon import db

# define a junction class between issue order product table
class ProductIssueOrder(db.Model):
    __tablename__ = 'product_issue_order'

    id = db.Column(db.Integer, primary_key=True)
    issue_order_id = db.Column(db.Integer, db.ForeignKey('issue_order.id'), primary_key=True)
    products_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Integer)

    issue_order = db.relationship('IssueOrder', backref='product_issue_order')
    product = db.relationship('Products', backref='product_issue_order')


    def __repr__(self):
        return '<ProductIssueOrder (IssueOrder={}, Product={}, Quantity={})>'.format(
                self.issue_order_id, self.products_id, self.quantity) """