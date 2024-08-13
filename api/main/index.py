from flask import Response
from flask import request,session,current_app
from flask import jsonify
from time import time
from base64 import b64decode
from . import main
from ..utils.redis import setHData,getHData,getttl
from ..utils.user import CaptchaGenerator

@main.route('/')
def index():
    key = current_app.config['SESSION_ID'];
    print(setHData('test',{
        'data': 1,
        'data2': 2
    },15))
    print(getHData('test','data'))
    return jsonify({
        'code': 200,
        'time': time(),
        'session_id': session[key]
    })


@main.route('/getCaptch')
def search():
    image,captcha = CaptchaGenerator(number=6,font='font/DK.ttf').generate_captcha();
    print(
        captcha
    )
    return Response(
        b64decode(image),
        mimetype='image/png'
    )
    