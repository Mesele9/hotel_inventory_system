"""empty message

Revision ID: 95417cb3f182
Revises: 906b484992be
Create Date: 2023-05-30 03:58:53.287546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95417cb3f182'
down_revision = '906b484992be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.alter_column('unit_price',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               type_=sa.Float(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.alter_column('unit_price',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=10, scale=2),
               existing_nullable=False)

    # ### end Alembic commands ###