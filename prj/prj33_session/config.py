#encoding: utf-8

from datetime import timedelta
import os

SECRET_KEY = os.urandom(24)
PERMANENT_SESSION_LIFETIME = timedelta(minutes=7)
