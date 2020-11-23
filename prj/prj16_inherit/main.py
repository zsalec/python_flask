from flask import Flask, render_template

app = Flask(__name__)


class Person(object):
    name = ''
    age = 0


class Student(Person):
    def study(self):
        print('studying')


class Teacher(Person):
    def teach(self):
        print("teaching")


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)