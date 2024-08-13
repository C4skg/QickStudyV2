from flask import request,session,current_app
from flask import jsonify,render_template
from time import time

from . import main
from ..utils.redis import setHData,getHData,getttl

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


@main.route('/search')
def search():
    return jsonify({
        'time': getttl('test')
    })