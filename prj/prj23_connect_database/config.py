DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'zs_alec'
PASSWORD = '19740512'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'dev_otms'
#SQLALCHEMY_DATABASE_URI = 'mysql://zs_alec:19740512@localhost/dev_otms'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False