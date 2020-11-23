from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


# user table
class User(db.Model):
    __tablename__ = 'py_demo1_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<User %d: %s>' % (self.id, self.username)


# article table
class Article(db.Model):
    __tablename__ = 'py_demo1_article_new'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('%s.id' % (User.__tablename__)))

    author = db.relationship('User', backref='articles')

    def __repr__(self):
        return '<Author %d: %s>' % (self.id, self.title)


db.create_all()


@app.route('/')
def index():
    # # insert User Tome
    # user_tom = User(username='Alec')
    # db.session.add(user_tom)
    # db.session.commit()

    # # insert article
    # article = Article(title='aaa', content='bbb', author_id=1)
    # db.session.add(article)
    # db.session.commit()

    # # query
    # article = Article.query.filter(Article.title == 'aaa').first()
    # author_id = article.author_id
    # author = User.query.filter(User.id == author_id).first()
    # print('username: %s' % author.username)

    # # insert ORM
    # article = Article(title='say hi', content='hello world')
    # article.author = User.query.filter(User.username == 'Alec').first()
    # db.session.add(article)
    # db.session.commit()

    # # query ORM
    # article = Article.query.filter(Article.title == 'say hi').first()
    # print('author: %s' % article.author.username)

    # query ORM back
    user = User.query.filter(User.username == 'Alec').first()
    articles = user.articles
    for article in articles:
        print('-'*10)
        print(article.title)

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
