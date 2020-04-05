# -*- coding: utf-8 -*-

from flask import Flask
from .models import db
from werkzeug.routing import BaseConverter


# 自定义正则转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        self.regex = args[0]

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.url_map.converters['re'] = RegexConverter

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from .views import bp
    app.register_blueprint(bp)

    return app
