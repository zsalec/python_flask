from html import escape

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        'username': 'Alec WANG',
        'sex': 'Male',
        'age': '46'
    }
    return render_template('index.html', username='Alec Wang', context=context)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
