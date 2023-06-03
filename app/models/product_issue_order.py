from app.dbcon import db

# define a junction class between issue order product table
class ProductIssueOrder(db.Model):
    __tablename__ = 'product_issue_order'

    issue_order_id = db.Column(db.Integer, db.ForeignKey('issue_order.id'), primary_key=True)
    products_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Integer)
