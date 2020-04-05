# -*- coding: utf-8 -*-
import re
from qrcode import QRCode, constants

def add_scheme(url):
    """给 URL 添加 scheme(qq.com -> http://qq.com)"""
    # 支持的 URL scheme
    # 常规 URL scheme
    scheme2 = re.compile(r'(?i)^[a-z][a-z0-9+.\-]*://')
    # 特殊 URL scheme
    scheme3 = ('git@', 'mailto:', 'javascript:', 'about:', 'opera:',
               'afp:', 'aim:', 'apt:', 'attachment:', 'bitcoin:',
               'callto:', 'cid:', 'data:', 'dav:', 'dns:', 'fax:', 'feed:',
               'gg:', 'go:', 'gtalk:', 'h323:', 'iax:', 'im:', 'itms:',
               'jar:', 'magnet:', 'maps:', 'message:', 'mid:', 'msnim:',
               'mvn:', 'news:', 'palm:', 'paparazzi:', 'platform:',
               'pres:', 'proxy:', 'psyc:', 'query:', 'session:', 'sip:',
               'sips:', 'skype:', 'sms:', 'spotify:', 'steam:', 'tel:',
               'things:', 'urn:', 'uuid:', 'view-source:', 'ws:', 'xfire:',
               'xmpp:', 'ymsgr:', 'doi:',
               )
    url_lower = url.lower()

    # 如果不包含规定的 URL scheme，则给网址添加 http:// 前缀
    scheme = scheme2.match(url_lower)
    if not scheme:
        for scheme in scheme3:
            url_splits = url_lower.split(scheme)
            if len(url_splits) > 1:
                break
        else:
            url = 'http://' + url
    return url

def qrcode_table(data, error_correct_level='H'):
    """生成 QR Code html 表格，可以通过 css 控制黑白块的显示"""
    if error_correct_level == 'L':
        error_correct_level = constants.ERROR_CORRECT_L
    elif error_correct_level == 'M':
        error_correct_level = constants.ERROR_CORRECT_M
    elif error_correct_level == 'Q':
        error_correct_level = constants.ERROR_CORRECT_Q
    else:
        error_correct_level = constants.ERROR_CORRECT_H

    qr = QRCode(error_correction=error_correct_level)
    qr.add_data(data)
    qr.make()

    html = '<table id="qrcode-table">'
    for r in range(qr.modules_count):
        html += "<tr>"
        for c in range(qr.modules_count):
            if (qr.modules[r][c] if qr.modules[r][c] != None else False):
                html += '<td class="dark" />'
            else:
                html += '<td class="white" />'
        html += '</tr>'
    html += '</table>'
    return html