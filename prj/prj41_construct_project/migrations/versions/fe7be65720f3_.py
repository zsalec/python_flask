"""empty message

Revision ID: fe7be65720f3
Revises: 624354e48ffc
Create Date: 2020-10-23 14:11:31.403847

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fe7be65720f3'
down_revision = '624354e48ffc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('py_demo1_prj_answer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False, comment='回答'),
    sa.Column('create_time', sa.DateTime(), nullable=False, comment='回答时间'),
    sa.Column('question_id', sa.Integer(), nullable=False, comment='问题ID'),
    sa.Column('author_id', sa.Integer(), nullable=False, comment='回答者ID'),
    sa.ForeignKeyConstraint(['author_id'], ['py_demo1_prj_user.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['py_demo1_prj_question.id'], ),
    sa.PrimaryKeyConstraint('id'),
    comment='问题回答'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('py_demo1_prj_answer')
    # ### end Alembic commands ###
