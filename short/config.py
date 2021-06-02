# -*- coding: utf-8 -*-
import os

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = os.environ.get('MYSQL_PASS')
DB_PORT = 3306
DB_DATABASE = 'test'
DB_CHARSET = 'utf8mb4'

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset={DB_CHARSET}"

SQLALCHEMY_TRACK_MODIFICATIONS = False