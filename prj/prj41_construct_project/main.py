#encoding: utf-8

from flask import Flask, render_template, request, redirect, session, url_for
from exts import db
from models import User, Question, Answer
from decorators import login_reqired
from datetime import datetime

import config

app = Flask(__name__, static_folder='./static', static_url_path='')
app.config.from_object(config)

db.init_app(app)


@app.context_processor
def my_context():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        # username = user.username
        return {'user': user}
    else:
        return {}


@app.route('/')
def index():
    print('homepage')
    context = {
        'questions': Question.query.order_by(Question.create_time.desc()).all()
    }
    return render_template('index.html', context=context)


@app.route('/login', methods=['get', 'post'])
def login():
    print('login page')
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            msg = '手机号码或密码错误，请确认后在登录'
            return render_template('login.html', msg=msg)


@app.route('/register', methods=['get', 'post'])
def register():
    print('register page')
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # validate telephone
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            msg = '该手机号码已经注册过了。'
            return render_template('register.html', msg=msg)
        if password1 != password2:
            msg = '两次密码不相同。'
            return render_template('register.html', msg=msg)
        user = User()
        user.telephone = telephone
        user.password = password2
        user.username = username
        db.session.add(user)
        db.session.commit()
        return redirect('login')


@app.route('/logout')
def logout():
    print('logout')
    if hasattr(session, 'user_id'):
        session.pop('user_id')
    return redirect(url_for('login'))


@app.route('/question', methods=['get', 'post'])
@login_reqired
def question():
    print('question page')
    if request.method == 'GET':
        return render_template('question.html')
    else:
        submitted_question = Question()
        submitted_question.title = request.form.get('title')
        submitted_question.content = request.form.get('content')
        submitted_question.create_time = datetime.now()
        submitted_question.author_id = session.get('user_id')
        db.session.add(submitted_question)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/detail/<question_id>')
@login_reqired
def detail(question_id):
    print('detail page')
    selected_question = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=selected_question)


@app.route('/add_answer', methods=['post'])
@login_reqired
def add_answer():
    print('add answer')
    answer = Answer()
    question_id = request.form.get('question_id')
    answer.question_id = question_id
    answer.content = request.form.get('content')
    answer.author_id = session.get('user_id')
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))


def decorate_my_log(func):
    def wrapper(*args, **kw):
        print('Hello world')
        return func(*args, **kw)
    return wrapper


@decorate_my_log
def decorate_run():
    print('run')


@decorate_my_log
def decorate_add(a, b):
    c = a + b
    print('result: %d' % c)


@app.route('/decorate')
def decorate_demo():
    decorate_run()
    decorate_add(1, 2)
    return 'decorator ok'


if __name__ == '__main__':
    app.run()
