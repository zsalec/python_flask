# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    # a = 1 / 0
    return 'hello, world!'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
