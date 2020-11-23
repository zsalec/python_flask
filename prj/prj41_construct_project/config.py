#encoding: utf-8

from datetime import timedelta
import os

# app
DEBUG = True

# session
SECRET_KEY = os.urandom(24)
PERMANENT_SESSION_LIFETIME = timedelta(hours=2)

# mysql
DB_USERNAME = 'zs_alec'
DB_PASSWORD = '19740512'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_DATABASE = 'spring'
DB_URI = 'mysql://%s:%s@%s:%d/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
