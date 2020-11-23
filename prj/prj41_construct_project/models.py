#encoding: utf-8

from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'py_demo1_prj_user'
    __table_args__ = ({'comment': '用户数据表'})
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False, comment='手机号码')
    username = db.Column(db.String(10), nullable=False, comment='用户名')
    password = db.Column(db.String(100), nullable=False, comment='密码')


class Question(db.Model):
    __tablename__ = 'py_demo1_prj_question'
    __table_args__ = {'comment': '提问问题清单'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False, comment='标题')
    content = db.Column(db.Text, nullable=False, comment='内容')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now, comment='创建时间')
    author_id = db.Column(db.Integer, db.ForeignKey('py_demo1_prj_user.id'), nullable=False, comment='发布者ID')

    author = db.relationship('User', backref=db.backref('questions'))


class Answer(db.Model):
    __tablename__ = 'py_demo1_prj_answer'
    __table_args__ = {'comment': '问题回答'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False, comment='回答')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now, comment='回答时间')
    question_id = db.Column(db.Integer, db.ForeignKey('py_demo1_prj_question.id'), nullable=False, comment='问题ID')
    author_id = db.Column(db.Integer, db.ForeignKey('py_demo1_prj_user.id'), nullable=False, comment='回答者ID')

    author = db.relationship('User', backref=db.backref('answers', order_by=create_time.desc()))
    question = db.relationship('Question', backref=db.backref('answers', order_by=create_time.desc()))
