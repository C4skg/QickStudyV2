from flask import Blueprint

user = Blueprint('user',__name__,url_prefix='/user')

from . import check,home,login,reset, signin