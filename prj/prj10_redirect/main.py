from html import escape

from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return 'Login'


@app.route('/question/<string:is_login>')
def question(is_login):
    if is_login == '1':
        return 'question'
    else:
        return redirect(url_for('login'))


@app.route('/myList')
def my_list():
    return 'list'


@app.route('/myList/<string:id>')
def my_list_item(string:id):
    return 'id %s' % id


@app.route('/article/<string:id>')
def article_info(id):
    return 'Your request parameter is %s' % escape(id)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/