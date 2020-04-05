# -*- coding: utf-8 -*-
import short_url
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shorten = db.Column(db.CHAR(8), nullable=False)
    expand = db.Column(db.TEXT, nullable=False)

    # def __init__(self, shorten, expand):
    #     self.shorten = shorten
    #     self.expand = expand

    def __repr__(self):
        return '<Urls %s>'.format(self.name)

    @classmethod
    def exist_expand(self, long_url):
        result = Urls.query.filter(Urls.expand == long_url).first()
        if result:
            return result
        return None

    @classmethod
    def add_url(self, long_url):
        model = Urls(shorten='', expand=long_url)
        db.session.add(model)
        db.session.commit()

        model = Urls.query.filter(Urls.expand == long_url).first()
        shorten = short_url.encode_url(model.id)
        model.shorten = shorten
        db.session.commit()

        return model

    @classmethod
    def get_expand(self, short_url):
        url = Urls.query.filter(Urls.shorten == short_url).first()
        return url
