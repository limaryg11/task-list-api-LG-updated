"""empty message

Revision ID: e05ebdd1a31a
Revises: 2138f82f12f9
Create Date: 2023-05-06 18:22:34.884859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e05ebdd1a31a'
down_revision = '2138f82f12f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
