'''
    用户中心页面 /user/home
'''
from flask import jsonify
from flask_login import login_required,current_user
from . import user

@user.route('/getUserInfo')
@login_required
def getUserInfo():
    return jsonify({
        'username': current_user.username,
        'nickname': current_user.nickname
    })
