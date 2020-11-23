from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

article_tag = db.Table('py_demo1_article1_tag1',
                       db.Column('article_id', db.Integer, db.ForeignKey('py_demo1_article1.id'), primary_key=True),
                       db.Column('tag_id', db.Integer, db.ForeignKey('py_demo1_tag1.id'), primary_key=True)
                       )


class Tag(db.Model):
    __tablename__ = 'py_demo1_tag1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


class Article(db.Model):
    __tablename__ = 'py_demo1_article1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)

    tags = db.relationship('Tag', secondary=article_tag,
                           backref=db.backref('articles', lazy='dynamic'),
                           lazy='dynamic')
    # tags = db.relationship('Tag', secondary=article_tag, backref='articles')


db.create_all()


@app.route('/')
def index():
    # # add new record
    # tag1 = Tag(name='111')
    # tag2 = Tag(name='222')
    #
    # article1 = Article(title='aaa')
    # article2 = Article(title='bbb')
    #
    # article1.tags.append(tag1)
    # article1.tags.append(tag2)
    #
    # article2.tags.append(tag1)
    # article2.tags.append(tag2)
    #
    # db.session.add(article1)
    # db.session.add(article2)
    #
    # db.session.add(tag1)
    # db.session.add(tag2)
    #
    # db.session.commit()

    # query ORM
    article = Article.query.filter(Article.title == 'aaa').first()
    tags = article.tags
    for tag in tags:
        print('tag: %s' % tag.name)

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
