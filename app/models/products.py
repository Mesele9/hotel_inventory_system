from app.dbcon import db
from app.models.purchase import ProductPurchaseOrder, PurchaseOrder
from app.models.issue import ProductIssueOrder


# define the product model
class Products(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    product_category = db.Column(db.String(50), nullable=False)
    uom = db.Column(db.String(50), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    reorder_level = db.Column(db.Integer, nullable=False)

    purchase_order = db.relationship('ProductPurchaseOrder', backref='products', lazy='dynamic', cascade='all, delete')
    issue_order = db.relationship('ProductIssueOrder', backref='products', lazy='dynamic', cascade='all, delete')


    def __repr__(self):
        return '{}: Available Quantity={}'.format(self.product_name, self.quantity)

