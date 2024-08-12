from flask import request,session,current_app
from flask import jsonify,render_template
from time import time

from . import main
from ..utils.redis import setData,getData

@main.route('/')
def index():
    key = current_app.config['SESSION_ID'];
    print(setData('test',1))
    print(getData('test'))
    return jsonify({
        'code': 200,
        'time': time(),
        'session_id': session[key]
    })