from flask import Flask
'''
flask plugins
'''
from flask_sqlalchemy import SQLAlchemy

from .config import getAppMode
from .errors import ParamError


db = SQLAlchemy();

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
        from .config import config
        app.config.from_object(
            config
        )
    elif envtype == "debug":
        from .config import debug
        app.config.from_object(
            debug
        )

    '''
        plugins init
    '''
    db.init_app(app)

    
    '''
        All blue_print register
    '''

    from .main import main as main_Blueprint
    
    app.register_blueprint(main_Blueprint)

    return app;