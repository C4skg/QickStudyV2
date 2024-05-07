from flask import session
from flask import jsonify,url_for
from flask_login import current_user
from flask_login import login_required,logout_user

from ..models import User
from ..statuscode import UserStatus
from .. import loginManager,flaskResponse
from . import user

@loginManager.unauthorized_handler
def handlerNeedsLogin():
    return jsonify({
        'status': 401,
        'message': '还未登录',
        'next': url_for('user.login')
    })

@user.route('/login',methods=['GET','POST'])
@flaskResponse.RequestEncoder()
def login(*args,**kwargs):
    if current_user.is_authenticated:
        return jsonify({
            "status": "ok",
            "message": "已登录，无需重复登录",
            "next": url_for("main.index")
        })
    else:
        user = User.query.filter(User.id==1);
        print(user)
        return 1

@user.route('/logout')
@login_required
def logout():
    try:
        logout_user();
        return jsonify({
            'status': 'ok',
            'code': UserStatus.OK,
            'message': '退出登录成功',
            'next': url_for('user.login')
        })
    except:
        pass;

    return jsonify({
        'status': 'error',
        'code': UserStatus.LOGOUTERROR,
        'message': '退出登录失败'
    })