"""Correct tables

Revision ID: 13266c7a03f2
Revises: 
Create Date: 2021-02-09 11:11:24.127299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13266c7a03f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('box',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('box_image',
    sa.Column('box_id', sa.Integer(), nullable=False),
    sa.Column('path', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['box_id'], ['box.id'], ),
    sa.PrimaryKeyConstraint('box_id', 'path')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('box_image')
    op.drop_table('box')
    # ### end Alembic commands ###