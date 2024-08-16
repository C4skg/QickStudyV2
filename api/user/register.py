from flask import (
    request,
    jsonify,
    url_for
)
from datetime import datetime
from sqlalchemy.exc import OperationalError
from ..models import User
from ..utils.user import (
    isVaildEmail,
    isVaildPassword,
    generateToekn,
    confirmToken
)
from ..errors import UserStatus,RegisterError,CaptchaError
from .. import db,flaskResponse
from . import user
from .verification import (
    checkCaptch,
    sendCaptchaCodeByEmail,
    checkCaptchaByEmail,
    cloudSendCaptchaEmail,
    getRegisterToken
)
from ..utils.time import checkTimeout


@user.route('/register/doregister',methods=['POST'])
@flaskResponse.RequestEncoder()
def doregister(*args,**kwargs):
    captcha = kwargs['form'].get('captcha');
    try:
       
        if not checkCaptchaByEmail(captcha):
            raise CaptchaError(code=UserStatus.CAPTCHA.CAPTCHAERROR,next=url_for('user.emailCaptch'));
        token = getRegisterToken();
        data = confirmToken(token);
        if not data:
            raise RegisterError(code=UserStatus.REGISTER.TOKENERROR);
        
        email = data.get('email');
        password = data.get('password');
        try:
            user = User.query.filter_by(
                email=email
            ).first();
        except OperationalError as execError:
            raise RegisterError(code=UserStatus.REGISTER.DATABASEERROR);

        if user:
            raise RegisterError(code=UserStatus.REGISTER.USEREXISTS);
        
        # begin register
        user = User(
            email = email.lower(),
            password = password,
            nickname = email
        );
        db.session.add(user);
        db.session.commit();
        return jsonify({
            'status': 'ok',
            'message': '用户注册成功',
            'next': url_for('user.login')
        })
    except RegisterError as error:
        return jsonify({
            'code': error.code,
            'message': error.message,
            'status': 'error',
            **error.kwrags
        }); 
    except OperationalError as error:
        return jsonify({
            'code': error.code,
            'message': error.message,
            'status': 'error'
        }); 
    except CaptchaError as error:
        return jsonify({
            'code': error.code,
            'message': error.message,
            'status': 'error',
            **error.kwrags
        }); 
    except:
        error = RegisterError(code=UserStatus.REGISTER.ERROR);
        return jsonify({
            'code': error.code,
            'status': 'error', 
            'message': error.message
        })
        

@user.route('/register/emailCaptch',methods=['POST'])
@flaskResponse.RequestEncoder()
def emailCaptch(*args,**kwrags):
    token = kwrags['form'].get('token',default='');
    data = confirmToken(token);
    try:
        if data == None:
            # token解密错误
            raise RegisterError(code=UserStatus.REGISTER.TOKENERROR);
        if checkTimeout(data.get('time'),3600):
            # token超时
            raise RegisterError(code=UserStatus.REGISTER.TOKENERROR);

        cloudSend,delayTime = cloudSendCaptchaEmail(email=data.get('email'),token=token);
        if not cloudSend:
            # 未到 60 秒 ，重复请求
            raise CaptchaError(code=UserStatus.CAPTCHA.TIMEERROR,time=delayTime);
        
        if not sendCaptchaCodeByEmail(
            email=data.get('email'),
            token=token,
            subject='用户注册确认',
            template='mail/captcha.html'
        ):
            raise CaptchaError(code=UserStatus.CAPTCHA.SENDERROR);
    except RegisterError as error:
        return jsonify({
            'code': error.code,
            'message': error.message,
            'status': 'error'
        });
    except CaptchaError as error:
        return jsonify({
            'code': error.code,
            'message': error.message,
            'status': 'error',
            **error.kwrags
        });

    return jsonify({
        'status': 'ok',
        'message': '邮件发送成功，请注册查收'
    });
    

@user.route('/register',methods=['POST'])
@flaskResponse.RequestEncoder()
def register(*args,**kwargs):
    captcha = kwargs['form'].get('captcha');
    email = kwargs['form'].get('email');
    password = kwargs['form'].get('password');
    try:
        if not checkCaptch(captcha):
            raise CaptchaError(code=UserStatus.CAPTCHA.CAPTCHAERROR);
    
        if not email or not password:
            raise RegisterError(code=UserStatus.REGISTER.PARAMERROR);

        if not isVaildEmail(email):
            raise RegisterError(code=UserStatus.REGISTER.EMAILERROR);
        
        if not isVaildPassword(password):
            raise RegisterError(code=UserStatus.REGISTER.PASSWORDERROR);
    
        try:
            user = User.query.filter_by(
                email=email
            ).first();
        except OperationalError as execError:
            raise RegisterError(code=UserStatus.REGISTER.DATABASEERROR);

        if user:
            raise RegisterError(code=UserStatus.REGISTER.USEREXISTS);

        token = generateToekn(
            email=email,
            password=password,
            time=datetime.now().timestamp()
        )


        return jsonify({
            'status': 'ok',
            'message': '',
            'token': token,
            'next': url_for('user.emailCaptch')
        })

    except RegisterError as error:
        return jsonify({
            'code': error.code,
            'message': error.message,
            'status': 'error'
        });
    except CaptchaError as error:
        return jsonify({
            'code': error.code,
            'message': error.message,
            'status': 'error'
        }); 
    except:
        error = RegisterError(code=UserStatus.REGISTER.ERROR);
        return jsonify({
            'code': error.code,
            'status': 'error', 
            'message': error.message
        })