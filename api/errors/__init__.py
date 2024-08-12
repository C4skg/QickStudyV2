from flask import Blueprint

error = Blueprint('error',__name__,url_prefix='/error')

from . import route
from .errors import *
from .statuscode import UserStatus