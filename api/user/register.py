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
    generateToekn
)
from ..utils.mail import send_email;
from ..errors import UserStatus,RegisterError
from .. import db,flaskResponse
from . import user

@user.route('/register',methods=['POST'])
@flaskResponse.RequestEncoder()
def register(*args,**kwargs):
    token = kwargs['form'].get('token');
    code = kwargs['form'].get('code');

    try:
        pass;
    except:
        pass;

    return {};
    

@user.route('/register/getLicense',methods=['POST'])
@flaskResponse.RequestEncoder()
def getRegisterLicense(*args,**kwargs):
    email = kwargs['form'].get('email');
    password = kwargs['form'].get('password');
    try:
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

        send_email(
            email,
            '用户注册确认',
            'mail/identifycode.html',
            host=request.url_root,
            code="123456"
        )

        return jsonify({
            'status': 'ok',
            'message': '验证码已发送至邮箱，请注意查收',
            'token': token,
            'next': url_for('user.register')
        })

    except RegisterError as error:
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