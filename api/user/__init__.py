from flask import Blueprint

user = Blueprint('user',__name__,url_prefix='/user')

from . import home,login, register,reset,verification