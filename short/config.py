# -*- coding: utf-8 -*-

DB_HOST = 'localhost'
DB_USER = ''
DB_PASS = ''
DB_PORT = 3306

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/short_url".format(DB_USER, DB_PASS, DB_HOST, DB_PORT)

SQLALCHEMY_TRACK_MODIFICATIONS = False