from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<is_login>')
def hello_world(is_login):
    if is_login == '1':
        user = {
            'username': 'Alec',
            'age': 46
        }
        return render_template('index.html', user=user)
    else:
        return render_template('index.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
