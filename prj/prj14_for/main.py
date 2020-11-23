from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    user = {
        'name': 'Alec',
        'sex': 'Male',
        'age': 48
    }
    web_sites = ['www.baidu.com', 'google.com']
    books = [
        {
            'name': 'XI YOU JI',
            'author': 'WU CHENG EN',
            'price': 108
        },
        {
            'name': 'SHUI HU ZHUAN',
            'author': 'SHI NAI AN',
            'price': 118
        }
    ]
    return render_template('index.html', user=user, websites=web_sites, books=books)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
