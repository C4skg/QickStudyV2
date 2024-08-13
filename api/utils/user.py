import re
import os
from flask import current_app
from authlib.jose import jwt, JoseError

def isVaildEmail(email:str) -> bool:
    email = email.strip().lower();
    pattern = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$';
    return re.match(
        pattern,
        email
    );

def isVaildPassword(password:str) -> bool:
    pattern = '^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,}$';
    return re.match(
        pattern,
        password
    )

def generateToekn(*args,**kwargs) -> str:
    header = { 'alg': 'HS256' };

    key = current_app.secret_key;
    print(kwargs)
    return jwt.encode(
        header=header,
        payload=kwargs,
        key='aasd',
        check=False
    ).decode();


def generateSessionId() -> str:
    return os.urandom(4).hex();


def generateCaptch(number:int=4) -> str:
    return None;

def generateCaptchImg(number:int=4) -> zip:
    return zip();