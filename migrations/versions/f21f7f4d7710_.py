"""empty message

Revision ID: f21f7f4d7710
Revises: 3af2c4d1926c
Create Date: 2018-05-02 09:41:40.315749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f21f7f4d7710'
down_revision = '3af2c4d1926c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###