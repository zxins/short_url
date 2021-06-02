# -*- coding: utf-8 -*-
import short_url
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class URLModel(db.Model):
    __tablename__ = 'url'

    id = db.Column(db.Integer, primary_key=True)
    shorten = db.Column(db.CHAR(8), nullable=False)
    expand = db.Column(db.TEXT, nullable=False)


    def __repr__(self):
        return '<Urls %s>' % self.shorten

    @classmethod
    def exist_expand(cls, long_url):
        result = URLModel.query.filter(URLModel.expand == long_url).first()
        if result:
            return result
        return None

    @classmethod
    def add_url(cls, long_url):
        model = URLModel(shorten='', expand=long_url)
        db.session.add(model)
        db.session.commit()

        model = URLModel.query.filter(URLModel.expand == long_url).first()
        shorten = short_url.encode_url(model.id)
        model.shorten = shorten
        db.session.commit()

        return model

    @classmethod
    def get_expand(cls, short_url):
        url = URLModel.query.filter(URLModel.shorten == short_url).first()
        return url
