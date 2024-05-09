from flask import session,request
from flask import jsonify,url_for
from flask_login import current_user
from flask_login import login_required,logout_user,login_user

from ..models import User,Logs
from ..errors import UserStatus
from ..errors import LoginError
from .. import db,loginManager,flaskResponse
from . import user

@loginManager.unauthorized_handler
def handlerNeedsLogin():
    return jsonify({
        'status': 401,
        'message': '还未登录',
        'next': url_for('user.login')
    }),401

@user.route('/login',methods=['POST'])
@flaskResponse.RequestEncoder()
def login(*args,**kwargs):
    if current_user.is_authenticated:
        return jsonify({
            "status": "ok",
            "message": "已登录，无需重复登录",
            "next": url_for("main.index")
        })

    try:
        username = kwargs.get('username');
        password = kwargs.get('password');
        if not username or not password:
            raise LoginError(code=UserStatus.LOGIN.PARAMERROR);
        
        user = User.query.filter(
            (User.username == username) | (User.email == username)
        ).first();

        if (
            (not user ) or (not user.verifyPassword(password))
        ):
            raise LoginError(code=UserStatus.LOGIN.PASSWORDERROR);
        
        if not user.cloudLogin():
            raise LoginError(code=UserStatus.LOGIN.REFUSE);
        
        login_user(user);
        login_log = Logs(
            context= f"用户登录成功",
            statuscode=UserStatus.LOGIN.OK
        )
        user.logs.append(login_log);
        db.session.merge(user);
        db.session.commit();

        return jsonify({
            'status': 'ok',
            'message': '登录成功',
            'next': url_for('main.index')
        })
    
    except LoginError as error:
        return jsonify({
            'code': error.code,
            'status': 'error',
            'message': error.message
        })

@user.route('/logout')
@login_required
def logout():
    try:
        logout_user();
        return jsonify({
            'status': 'ok',
            'code': UserStatus.LOGOUT.OK,
            'message': '退出登录成功',
            'next': url_for('user.login')
        })
    except Exception as e:
        '''
            记录日志
        '''
        errorlog = Logs(
            context = f"{str(e)}",
            statuscode = UserStatus.LOGOUT.ERROR
        )
        user = current_user.logs.append(
            errorlog
        )
        db.session.merge(user);
        db.session.commit();

    return jsonify({
        'status': 'error',
        'code': UserStatus.LOGOUTERROR,
        'message': '退出登录失败'
    })