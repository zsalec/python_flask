#encoding: utf-8

from flask import Flask, render_template, g, session, redirect, url_for, request
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)


@app.before_request
def before_request():
    print('before request')
    if session.get('username'):
        g.username = session.get('username')


@app.context_processor
def my_context_processor():
    print('context processor')
    username = session.get('username', '')
    print(session.get('username'))
    # if username:
    return {'username': username}


@app.route('/')
def index():
    print('index')
    return render_template('index.html')
    # return 'index'


@app.route('/login', methods=['get', 'post'])
def login():
    print('login')
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print('username: %s, password: %s' % (username, password))
        session['username'] = username
        return 'congratulation. login successfully'
    # return 'login'


@app.route('/edit')
def edit():
    print('edit')
    return render_template('edit.html')
    # return 'edit'


if __name__ == '__main__':
    app.run(debug=True)
