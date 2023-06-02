from datetime import datetime
from app.dbcon import db
from flask_login import current_user
from app.models import Products, Users

# define the purchaseorder model
class PurchaseOrder(db.Model):
    __tablename__ = 'purchase_order'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, nullable=False, default=datetime.now().date())
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    supplier = db.Column(db.String(50))
    status = db.Column(db.String(20), nullable=False, default='created')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), default=current_user.id)


    products = db.relationship("Products", back_populates="purchaseorders")
    users = db.relationship("Users", back_populates="orders")



""" # define PurchaseOrderItem model
class PurchaseOrderItem(db.Model):
    __tablename__ = 'purchase_order_item'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('purchase_order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)
    unit_price = Column(DECIMAL(10, 2))

 """