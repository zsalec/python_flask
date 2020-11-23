#encoding: utf-8

from flask_script import Manager

db_manager = Manager()

@db_manager.command
def init():
    print('finished to initialize database.')


@db_manager.command
def migrate():
    print('migrate database')
