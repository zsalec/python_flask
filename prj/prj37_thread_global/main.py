#encoding: utf-8

from flask import Flask, render_template, g, request
from ulog import login_log

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            # login_log(username)
            g.username = username
            g.ip = 'localhost'
            login_log()
            return 'congratulation. login successfully'
        else:
            return 'Login fail'


if __name__ == '__main__':
    app.run(debug=True)
