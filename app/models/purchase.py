from datetime import datetime
from app.dbcon import db


# define the purchaseorder model
class PurchaseOrder(db.Model):
    __tablename__ = 'purchase_order'
    
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, nullable=False, default=datetime.now().date())
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    supplier = db.Column(db.String(50))
    status = db.Column(db.String(20), nullable=False, default='created')


    users = db.relationship('Users', backref='purchase_order')   
    products = db.relationship('ProductPurchaseOrder', backref='purchase_order') 


    def __repr__(self):
        return '<Purchase Order: {} : {}>'.format(self.id, self.status)
    

