from exts import db


class Article(db.Model):
    __tablename__ = 'py_demo1_article1'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
