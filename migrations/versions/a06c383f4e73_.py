"""empty message

Revision ID: a06c383f4e73
Revises: f8951ff2e608
Create Date: 2023-06-03 18:32:19.288295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a06c383f4e73'
down_revision = 'f8951ff2e608'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('issue_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('requested_date', sa.Date(), nullable=False),
    sa.Column('requested_by', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['requested_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchase_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.Date(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('supplier', sa.String(length=50), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_issue_order',
    sa.Column('issue_order_id', sa.Integer(), nullable=False),
    sa.Column('products_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['issue_order_id'], ['issue_order.id'], ),
    sa.ForeignKeyConstraint(['products_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('issue_order_id', 'products_id')
    )
    op.create_table('product_purchase_order',
    sa.Column('purchase_order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['purchase_order_id'], ['purchase_order.id'], ),
    sa.PrimaryKeyConstraint('purchase_order_id', 'product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_purchase_order')
    op.drop_table('product_issue_order')
    op.drop_table('purchase_order')
    op.drop_table('issue_order')
    # ### end Alembic commands ###
