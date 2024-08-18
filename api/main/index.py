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
    return jsonify({
        'code': 200,
        'time': time(),
        'session_id': session[key]
    })