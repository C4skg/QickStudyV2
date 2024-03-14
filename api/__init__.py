from flask import Flask
from os import getenv
from dotenv import load_dotenv

from .errors import ParamError

load_dotenv();

def create_app( envtype:str = None ):
    """
    this function will create flask app
    if envtype is None , we will get envtype from system
    you can set system env or write it in .env file
    """

    if envtype is None:
        envtype = getenv('app_mode')

    if envtype not in ('build','debug'):
        raise ParamError(envtype=envtype)
    
    app = Flask(__name__)
    if envtype == 'build':
        from .config import config
        app.config.from_object(
            config
        )
    elif envtype == 'debug':
        from .config import debug
        app.config.from_object(
            debug
        )

    from .main import main as main_Blueprint
    
    app.register_blueprint(main_Blueprint)

    return app;