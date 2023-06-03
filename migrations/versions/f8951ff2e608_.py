"""empty message

Revision ID: f8951ff2e608
Revises: 9de84701e74f
Create Date: 2023-06-03 16:57:11.144335

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = 'f8951ff2e608'
down_revision = '9de84701e74f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_issue_order')
    op.drop_table('issue_order')
    op.execute(text("DROP TABLE purchase_order CASCADE"))
    op.drop_table('product_purchase_order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_purchase_order',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('purchase_order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='product_purchase_order_product_id_fkey'),
    sa.ForeignKeyConstraint(['purchase_order_id'], ['purchase_order.id'], name='product_purchase_order_purchase_order_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='product_purchase_order_pkey')
    )
    op.create_table('purchase_order',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('supplier', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], name='purchase_order_created_by_fkey'),
    sa.PrimaryKeyConstraint('id', name='purchase_order_pkey')
    )
    op.create_table('issue_order',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('issue_order_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('requested_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('requested_by', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['requested_by'], ['users.id'], name='issue_order_requested_by_fkey'),
    sa.PrimaryKeyConstraint('id', name='issue_order_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('product_issue_order',
    sa.Column('issue_order_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('products_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['issue_order_id'], ['issue_order.id'], name='product_issue_order_issue_order_id_fkey'),
    sa.ForeignKeyConstraint(['products_id'], ['products.id'], name='product_issue_order_products_id_fkey'),
    sa.PrimaryKeyConstraint('issue_order_id', 'products_id', name='product_issue_order_pkey')
    )
    # ### end Alembic commands ###
