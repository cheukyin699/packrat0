"""Add field to box

Revision ID: 398a47dddce0
Revises: 13266c7a03f2
Create Date: 2021-02-09 12:17:13.470769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '398a47dddce0'
down_revision = '13266c7a03f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('box', sa.Column('description', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('box', 'description')
    # ### end Alembic commands ###
