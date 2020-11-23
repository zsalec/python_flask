#encoding: utf-8

from flask_script import Manager
from main import app
from db_script import db_manager

manager = Manager(app)

manager.add_command('db', db_manager)


@manager.command
def runserver():
    print('server is running...')


if __name__ == '__main__':
    manager.run()
