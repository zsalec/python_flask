#encoding: utf-8

from exts import db
from flask import Flask
from models import Article
import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

# with app.app_context():
#     db.create_all()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
