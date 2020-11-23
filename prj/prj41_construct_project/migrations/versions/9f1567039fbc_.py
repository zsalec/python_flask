"""empty message

Revision ID: 9f1567039fbc
Revises: c2088518d4d2
Create Date: 2020-10-22 16:35:08.673195

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9f1567039fbc'
down_revision = 'c2088518d4d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('py_demo1_prj_user', 'password',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False,
               existing_comment='密码')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('py_demo1_prj_user', 'password',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True,
               existing_comment='密码')
    # ### end Alembic commands ###
