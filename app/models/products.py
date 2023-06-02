from app.dbcon import db


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


    def __repr__(self):
        return '<Product (Name={}), (Category={}), (Quantity={}>)'.format(
                self.id, self.product_name, self.product_category, self.unit_price, self.quantity)
