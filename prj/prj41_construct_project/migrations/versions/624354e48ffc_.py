"""empty message

Revision ID: 624354e48ffc
Revises: e28f65d488be
Create Date: 2020-10-23 09:53:39.626645

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '624354e48ffc'
down_revision = 'e28f65d488be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('py_demo1_prj_question',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False, comment='标题'),
    sa.Column('content', sa.Text(), nullable=False, comment='内容'),
    sa.Column('create_time', sa.DateTime(), nullable=False, comment='创建时间'),
    sa.Column('author_id', sa.Integer(), nullable=False, comment='发布者ID'),
    sa.ForeignKeyConstraint(['author_id'], ['py_demo1_prj_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    comment='提问问题清单'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('py_demo1_prj_question')
    # ### end Alembic commands ###
