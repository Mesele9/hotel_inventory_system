from datetime import datetime
from app.dbcon import db
from flask_login import current_user

# define a junction class between purchase order product table
class ProductPurchaseOrder(db.Model):
    __tablename__ = 'product_purchase_order'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    purchase_order_id = db.Column(db.Integer, db.ForeignKey('purchase_order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return '<ProductPurchaseOrder (PurchaseOrder={}, Product={}, Quantity={})>'.format(
                self.purchase_order_id, self.product_id, self.quantity)


# define the purchaseorder model
class PurchaseOrder(db.Model):
    __tablename__ = 'purchase_order'
    
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, nullable=False, default=datetime.now().date())
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    supplier = db.Column(db.String(50))
    status = db.Column(db.String(20), nullable=False, default='created')


    users = db.relationship('Users', backref='purchase_order')   
    products = db.relationship('ProductPurchaseOrder', backref='purchase_order', lazy='dynamic', cascade='all, delete') 


    def __repr__(self):
        return '<Purchase Order: ID={} User ID={}: Status={}>'.format(self.id, self.created_by, self.status)
    

    

