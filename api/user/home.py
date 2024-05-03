'''
    用户中心页面 /user/home
'''
from flask import jsonify
from flask_login import login_required
from . import user

@user.route('/')
@login_required
def home():
    pass;