#encoding: utf-8

from flask import g


def login_log(username):
    print('user %s log' % username)


def login_log():
    print('username: %s, ip: %s' % (g.username, g.ip))
