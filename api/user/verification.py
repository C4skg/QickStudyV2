from flask import current_app,request
from flask import jsonify
from flask import Response
from flask_login import current_user
from base64 import b64decode

from ..utils.redis import getHData,setHData,getttl
from ..utils.user import CaptchaGenerator
from ..utils.mail import send_email

from . import user

def cloudSendCaptchaEmail(email:str,token:str) -> tuple:
    __group__ = 'Register'

    revokeTime = getttl(__group__);
    delaytime = 60 - (60*5 - revokeTime);
    if delaytime < 0:
        return True,delaytime;

    return False,delaytime;

def sendCaptchaCodeByEmail(email:str,token:str,subject:str,template:str) -> bool:
    __group__ = 'Register'

    captcha = CaptchaGenerator(
        number=6,
        numericOnly=True
    ).generate_captcha_code();
    status = setHData(
        __group__,
        {
            'email': email.lower(),
            'captcha': captcha.lower(),
            'token': token
        },
        60 * 5
    )
    if not status:
        return False;

    send_email(
        email,
        subject,
        template=template,
        host=request.url_root,
        code=captcha
    )
    return True; 

def getRegisterToken():
    __group__ = 'Register'

    _store_token = getHData(__group__,'token',None);
    return _store_token;

def checkCaptchaByEmail(captcha:str) -> bool:
    __group__ = 'Register'
    
    if type(captcha) != str:
        return False;

    _store_captcha = getHData(__group__,'captcha',None);
    # _store_email = getHData('emailCaptcha','email',None);
    if not _store_captcha:
        return False;

    captcha = captcha.lower();

    return (
        (captcha == _store_captcha)
    )


def checkCaptch(captcha:str) -> bool:
    _store_captcha = getHData('captchimage','captcha');
    if not _store_captcha:
        return False;

    captcha = captcha.lower();
    updateCaptch();
    return (
        _store_captcha == captcha
    );


def updateCaptch() -> str:
    image,captcha = CaptchaGenerator(
        number=6,
        font='font/DK.ttf'
    ).generate_captcha();

    status = setHData(
        'captchimage',
        {
            "image": image,
            "captcha": captcha.lower()
        },
        60 * 5
    )
    if not status:
        return ""
    
    return image;


@user.route('/updateCaptch')
def refresh():
    status = updateCaptch();
    if not status:
        return jsonify({
            'code': 500,
            'status': 'error',
            'message': '更新失败'
        })
    
    return jsonify({
        'code': 200,
        'status': 'ok',
        'message': '更新成功'
    })

@user.route('/getCaptchaImage')
def getCaptchaImage():
    data = getHData('captchimage',"image",'');
    if not data:
        data = (updateCaptch());
    return jsonify({
        'image': data,
        'format': 'base64',
        'filetype': 'png'
    })