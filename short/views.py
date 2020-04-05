# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, abort, jsonify, redirect
from .utils import add_scheme, qrcode_table
from .models import Urls

bp = Blueprint('short_bp', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/shorten', methods=['POST'])
def shorten():
    url = request.form.get('url')
    if not url:
        try:
            data = request.get_json()
            url = data['url']
        except:
            abort(400)

    url = add_scheme(url)

    # 判断是否已存在相应的数据
    exists = Urls.exist_expand(url)
    if exists:
        shorten = exists.shorten
    else:
        shorten = Urls.add_url(url).shorten

    base_url = request.base_url.rsplit('/', 1)[0]
    shorten = base_url + '/' + shorten

    content_type = request.headers.get('Content-Type')

    if content_type == 'application/json':
        return jsonify({'shorten': shorten, 'expand': url})

    data = {
        'url': shorten,
        'qr_table': qrcode_table(shorten),
    }
    return render_template('shorten.html', **data)


@bp.route('/<re("[a-zA-Z0-9]{5,}"):shorten>', methods=['GET'])
def expand(shorten):
    shorten = Urls.get_expand(shorten)
    if not shorten:
        abort(404)
    return redirect(shorten.expand)


@bp.route('/expand', methods=['POST'])
def expand_api():
    param = request.form.get('shorten')
    if not param:
        try:
            data = request.get_json()
            param = data['shorten']
        except:
            abort(400)

    shorten = param.strip().strip('/').rsplit('/', 1)[-1]
    shorten = Urls.get_expand(shorten)
    if not shorten:
        return jsonify({'error_code': 404, 'error_msg': 'shorten is not found'})

    expand = shorten.expand
    base_url = request.base_url.rsplit('/', 1)[0]
    shorten = base_url + '/' + shorten.shorten
    return jsonify({'shorten': shorten, 'expand': expand})
