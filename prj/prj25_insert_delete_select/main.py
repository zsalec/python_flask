from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import config

app = Flask('__name__')
app.config.from_object(config)

db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'py_demo1_article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

db.create_all()


@app.route('/')
def hello_world():
    # # insert
    # article = Article(title='aaa', content='bbb')
    # db.session.add(article)
    # db.session.commit()

    # # query
    # article = Article.query.filter(Article.title == 'aaa').first()
    # print('title: %s' % article.title)
    # print('content: %s' % article.content)

    # # update
    # article = Article.query.filter(Article.title == 'aaa').first()
    # article.content = 'new content'
    # db.session.commit()

    # delete
    article = Article.query.filter(Article.title == 'aaa').first()
    db.session.delete(article)
    db.session.commit()

    return 'HHello, world!'


if __name__ == '__main__':
    app.run(debug=True)