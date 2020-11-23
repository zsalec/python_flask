#encoding: utf-8

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    print(request.args)
    return 'keywords: %s' % request.args.get('q')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print(request.form, username, password)
        return 'ok (username: %s, password: %s)' % (username, password)


if __name__ == '__main__':
    app.run(debug=True)
