from html import escape

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(url_for('my_list'))
    print(url_for('my_list', id='abc'))
    return 'Hello, world!'


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