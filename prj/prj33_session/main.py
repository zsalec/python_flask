#encoding: utf-8

from flask import Flask, session
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    session['username'] = 'Alec Flask'
    session.permanent = True
    return 'add session'


@app.route('/get')
def get():
    username = session.get('username')
    return 'get session: %s' % username


@app.route('/remove')
def remove():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return 'remove session key'


@app.route('/clear')
def clear():
    print(session.get('username'))
    session.clear()
    print(session.get('username'))
    return 'clear all session'


if __name__ == '__main__':
    app.run(debug=True)
