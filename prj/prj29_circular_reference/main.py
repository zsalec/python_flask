from exts import db
from flask import Flask
from models import Article
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    article = Article.query.first()
    print('title %s' % article.title)
    return 'ok title %s' % article.title


if __name__ == '__main__':
    app.run(debug=True)
