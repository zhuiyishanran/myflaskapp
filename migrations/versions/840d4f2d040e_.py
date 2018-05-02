"""empty message

Revision ID: 840d4f2d040e
Revises: 62bb06b31505
Create Date: 2018-05-02 14:41:57.270621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '840d4f2d040e'
down_revision = '62bb06b31505'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###