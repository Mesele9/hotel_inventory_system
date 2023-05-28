""" from app.dbcon import db

# define issueorder model
class IssueOrder(Base):
    __tablename__ = 'issue_order'

    id = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False, default=datetime.now().date())
    recipient = Column(String(50))
    status = Column(ENUM('PREPARED', 'APPROVED', 'RECEIVED', name='issue_enum'), default='PREPARED')
    created_by = Column(Integer, ForeignKey('users.id'))

    users = relationship('Users')


# define issueorderitem model
class IssueOrderItem(Base):
    __tablename__ = 'issue_order_item'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('issue_order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer)
    unit_price = Column(DECIMAL(10, 2))
 """
