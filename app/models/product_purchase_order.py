from datetime import datetime
from app.dbcon import db


# define a junction class between purchase order product table
class ProductPurchaseOrder(db.Model):
    __tablename__ = 'product_purchase_order'

    purchase_order_id = db.Column(db.Integer, db.ForeignKey('purchase_order.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Integer)

    
