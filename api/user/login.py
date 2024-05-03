from flask import jsonify,url_for
from flask_login import current_user
from flask_login import login_required

from .. import loginManager
from . import user


@loginManager.unauthorized_handler
def handlerNeedsLogin():
    return jsonify({
        'status': 401,
        '': '',
        'next': url_for('user.login')
    })

@user.route('/login',methods=['POST'])
def login():
    if current_user.is_authenticated:
        return ;
    