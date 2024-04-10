from flask import Blueprint

user = Blueprint('user',__name__)

from . import check,home,login,register,reset