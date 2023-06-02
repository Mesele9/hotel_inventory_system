from datetime import datetime
from app.dbcon import db



# define a junction table between purchase order product table
product_purchase_order = db.Table('product_purchase_order',
                                  db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
                                  db.Column('purchase_order_id', db.Integer, db.ForeignKey('purchase_order.id'), primary_key=True),
                                  db.Column('quantity', db.Integer, nullable=False),
                                  extend_existing=True
                                )


# define the purchaseorder model
class PurchaseOrder(db.Model):
    __tablename__ = 'purchase_order'
    
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, nullable=False, default=datetime.now().date())
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    supplier = db.Column(db.String(50))
    status = db.Column(db.String(20), nullable=False, default='created')


    users = db.relationship('Users', backref='purchase_order')    
    products = db.relationship('Products', secondary=product_purchase_order, backref=db.backref('purchase_order', lazy='dynamic'),
                               cascade='all, delete-orphan')



""" # define PurchaseOrderItem model
class PurchaseOrderItem(db.Model):
    __tablename__ = 'purchase_order_item'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('purchase_order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False) """