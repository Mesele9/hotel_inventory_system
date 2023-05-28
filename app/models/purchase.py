""" from app.dbcon import db


# define the purchaseorder model
class PurchaseOrder(db.Model):
    __tablename__ = 'purchase_order'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, nullable=False, default=datetime.now().date())
    supplier = Column(String(50))
    status = Column(ENUM('PREPARED', 'APPROVED', 'PURCHASED', name='purchaser_enum'), default='PREPARED')
    created_by = Column(Integer, ForeignKey('users.id'))

    users = relationship('Users')


# define PurchaseOrderItem model
class PurchaseOrderItem(db.Model):
    __tablename__ = 'purchase_order_item'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('purchase_order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)
    unit_price = Column(DECIMAL(10, 2))

 """