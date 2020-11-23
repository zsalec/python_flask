#encoding: utf-8

from flask_script import Manager
from main import app
from flask_migrate import Migrate, MigrateCommand
from exts import db
from models import Article

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
