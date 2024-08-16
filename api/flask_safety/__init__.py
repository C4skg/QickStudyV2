"""
flaskext.Crypto
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

from ._request import Loader
from .response import StatusCode,ServerResponse

class FlaskCrypto(object):

    def __init__(self,app = None) -> None:

        if app is not None:
            self.init_app(app);


    def init_app(self,app = None):
        if app is None:
            return False;

        @app.before_request
        def _ext_before_request_handle(*args,**kwrags):
            if request.method == "POST":
                pass;
        

    def RequestEncoder(self):
        def decorator(func):
            @wraps(func)
            def wrapper(*args,**kwargs):
        
                " update the request data "
                kwargs.update(
                    Loader(request).to_dict()
                )
                recall = func(*args,**kwargs)
                if type(recall) == dict:
                    recall = jsonify(recall);
                
                data = json.loads(recall.data.decode());
                if data.get('code') is None:
                    data['code'] = StatusCode.OK;
                    recall.data = json.dumps(data).encode()

                return ServerResponse(recall.json).response();
        
            " Function Wrapper "
            return wrapper;

        return decorator;
