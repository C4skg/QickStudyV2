from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_cors import CORS
from .flask_response import FlaskCrypto

from .config import getAppMode
from .errors.errors import ParamError


db = SQLAlchemy();
loginManager = LoginManager();
flaskResponse = FlaskCrypto();
mail = Mail();
cors = CORS();

def create_app( envtype:str = None ):
    """
    this function will create flask app
    if envtype is None , we will get envtype from system
    you can set system env or write it in .env file
    """

    if envtype is None:
        envtype = getAppMode();

    if envtype not in ("build","debug"):
        raise ParamError(envtype=envtype)
    
    app = Flask(__name__)
    if envtype == "build":
        from .config import build
        app.config.from_object(
            build
        )
    elif envtype == "debug":
        from .config import debug
        app.config.from_object(
            debug
        )

    '''
        plugins init
    '''
    db.init_app(app);
    mail.init_app(app);
    loginManager.init_app(app);
    flaskResponse.init_app(app);
    cors.init_app(app);
    
    '''
        All blue_print register
    '''

    from .main import main as main_Blueprint
    from .user import user as user_Blueprint
    from .errors import error as error_Blueprint
    app.register_blueprint(main_Blueprint)
    app.register_blueprint(user_Blueprint)
    app.register_blueprint(error_Blueprint)

    return app;