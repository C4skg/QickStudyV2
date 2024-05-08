'''
    用户中心页面 /user/home
'''
from flask import jsonify
from flask_login import login_required
from . import user

@user.route('/')
@login_required
def home():
    return jsonify({
        'flag': 1
    })

@user.route('/<int:id>')
def home_by_id(id:int):
    return jsonify({
        'flag': None,
        'id': id
    })