""" from datetime import datetime
from app.dbcon import db


# define a junction class between purchase order product table
class ProductPurchaseOrder(db.Model):
    __tablename__ = 'product_purchase_order'

    id = db.Column(db.Integer, primary_key=True)
    purchase_order_id = db.Column(db.Integer, db.ForeignKey('purchase_order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer)

    
    purchase_order = db.relationship('PurchaseOrder', backref='product_purchase_order')
    products = db.relationship('Products', backref='product_purchase_order')


    def __repr__(self):
        return '<ProductPurchaseOrder (PurchaseOrder={}, Product={}, Quantity={})>'.format(
                self.purchase_order_id, self.product_id, self.quantity) """