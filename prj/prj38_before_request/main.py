#encoding: utf-8

from flask import Flask, render_template, request, session, redirect, url_for, g
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

@app.route('/')
def index():
    print('index')
    return 'index'


@app.route('/login', methods=['GET', 'POST'])
def login():
    print('login')
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print('username: %s, password: %s' % (username, password))
        if username == 'admin' and password == 'admin':
            session['username'] = username
            return 'congratulation. successfully login!'
        else:
            return 'login fail!'


@app.route('/edit')
def edit():
    if hasattr(g, 'username'):
        print('login username: %s' % session.get('username'))
        return 'successfully edited'
    else:
        return redirect(url_for('login'))


@app.before_request
def my_before():
    print('hello world!')
    if session.get('username'):
        g.username = session.get('username')


if __name__ == '__main__':
    app.run(debug=True)
