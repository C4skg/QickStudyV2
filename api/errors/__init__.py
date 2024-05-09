from flask import Blueprint

error = Blueprint('error',__name__,url_prefix='/error')

from . import route
from .errors import ParamError,LoginError
from .statuscode import UserStatus