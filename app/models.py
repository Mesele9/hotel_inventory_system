from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# create a base class for declarative models
Base = declarative_base()


# define the product model
class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    category = Column(String(255))
    quantity = Column(Integer)
    unit_price = Column(DECIMAL(10, 2))


# define the purchaseorder model
class PurchaseOrder(Base):
    __tablename__ = 'purchase_order'

    id = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False, default=datetime.now().date())
    supplier = Column(String(255))
    status = Column(String(50))
    created_by = Column(Integer, ForeignKey('user.id'))

    user = relationship('User')


# define PurchaseOrderItem model
class PurchaseOrderItem(Base):
    __tablename__ = 'purchase_order_item'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('purchase_order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)
    unit_price = Column(DECIMAL(10, 2))


# define issueorder model
class IssueOrder(Base):
    __tablename__ = 'issue_order'

    id = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False, default=datetime.now().date())
    recipient = Column(String(255))
    status = Column(String(50))
    created_by = Column(Integer, ForeignKey('user.id'))

    user = relationship('User')


# define issueorderitem model
class IssueOrderItem(Base):
    __tablename__ = 'issue_order_item'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('issue_order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)
    unit_price = Column(DECIMAL(10, 2))


# define the user model
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)
