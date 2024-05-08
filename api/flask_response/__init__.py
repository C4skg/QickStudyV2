"""
flaskext.crypter
---------------------
This module could encode your data and also decode the data

该插件会接管全局的Server属性
优先级如下：
    单个路由方法体 > flask_response > flask
"""
import json
from flask import current_app,request,session
from flask import Blueprint
from flask import jsonify,abort
from functools import wraps
from hashlib import md5
from time import time
from werkzeug.serving import WSGIRequestHandler
from .response import ServerResponse,StatusCode


class FlaskResponse(object):

    def __init__(self,app = None) -> None:

        if app is not None:
            self.init_app(app);


    def init_app(self,app):
        pass;


    def RequestEncoder(self,errorCode=52103,RandomServer=True):
        def decorator(func):
            @wraps(func)
            def wrapper(*args,**kwargs):
                if request.method != 'POST':
                    # abort(500)
                    pass;
                '''
                    获取路由返回值
                '''
                formData = dict(request.form);
                kwargs.update(formData);
                
                r = func('after test',*args,**kwargs)
                if type(r) == dict:
                    r = jsonify(r);
                
                data = json.loads(r.data.decode());
                if data.get('code') is None:
                    data['code'] = StatusCode.OK;
                    r.data = json.dumps(data).encode()

                return ServerResponse(r.json).response();
        
            '''
                function wrapper
            '''
            return wrapper;

        return decorator;
