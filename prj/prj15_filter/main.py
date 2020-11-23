from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    comments = [
        {
            'user': 'Tom',
            'content': 'comment'
        },
        {
            'user': 'Jerry',
            'content': 'Bad'
        }
    ]
    return render_template('index.html', avatar='https://yichengzhang.cn/uploads/croppedImg_6548.jpeg', comments=comments)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
