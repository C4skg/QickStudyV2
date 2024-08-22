from flask import session,request
from flask import jsonify,url_for
from sqlalchemy.exc import OperationalError
from flask_login import current_user
from flask_login import login_required,logout_user,login_user

from ..models import User,Logs
from ..errors import UserStatus,LoginError,CaptchaError
from ..utils.log import LOG_LEVEL,LOGGER
from .verification import checkCaptch 
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
        username = kwargs['form'].get('username');
        password = kwargs['form'].get('password');
        captcha = kwargs['form'].get('captcha');

        if not checkCaptch(captcha):
            raise CaptchaError(code=UserStatus.CAPTCHA.CAPTCHAERROR);
    
        if not username or not password:
            raise LoginError(code=UserStatus.LOGIN.PARAMERROR);
        
        try:
            user = User.query.filter(
                (User.username == username) | (User.email == username)
            ).first();
        except OperationalError as execError:
            raise LoginError(code=UserStatus.LOGIN.DATABASEERROR);

        if (
            (not user ) or (not user.verifyPassword(password))
        ):
            raise LoginError(code=UserStatus.LOGIN.PASSWORDERROR);
        
        if not user.cloudLogin():
            raise LoginError(code=UserStatus.LOGIN.REFUSE);
        
        login_user(user);
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
    except CaptchaError as error:
        return jsonify({
            'code': error.code,
            'status': 'error',
            'message': error.message
        })
    except Exception as e:
        errorlog = Logs(
            context = f"{str(e)}",
            statuscode = UserStatus.LOGOUT.ERROR,
            level = LOG_LEVEL.ERROR
        )
        error = LoginError(code=UserStatus.LOGIN.ERROR);
        db.session.merge(errorlog);
        db.session.commit();
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
            statuscode = UserStatus.LOGOUT.ERROR,
            level = LOG_LEVEL.CRITICAL
        )
        db.session.merge(errorlog);
        db.session.commit();

    return jsonify({
        'status': 'error',
        'code': UserStatus.LOGOUTERROR,
        'message': '退出登录失败'
    })