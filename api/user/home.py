'''
    用户中心页面 /user/home
'''
from flask import jsonify
from flask_login import login_required,current_user

from . import user
from .error import getUserInfoError
from ..models import User



@user.route('/getUserInfo')
@user.route('/getUserInfo/<int:id>')
@login_required
def getUserInfo(id:int):
    if not id:
        return jsonify({
            'id': current_user.id,
            'nickname': current_user.nickname,
            'avatar': current_user.avatar,
            'signatureText': current_user.signatureText
        })
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            raise getUserInfoError(code=getUserInfoError.NOUSER);
    except getUserInfoError as error:
        return jsonify({
            'code': error.code,
            'status': 'error',
            'message': error.message
        })

