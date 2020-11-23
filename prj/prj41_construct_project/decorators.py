#encoding: utf-8

from flask import session, redirect, url_for
from functools import wraps


# login limit
def login_reqired(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
