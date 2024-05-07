from os import urandom,getenv
from dotenv import load_dotenv
load_dotenv();
class Config:
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD") or "admin@QickStudy"

    #email config
    MAIL_ENABLE = getenv("MAIL_ENABLE") == "true"
    MAIL_SERVER = getenv("MAIL_SERVER")
    MAIL_PORT = getenv("MAIL_PORT")
    MAIL_USERNAME = getenv("MAIL_USERNAME")
    MAIL_PASSWORD = getenv("MAIL_PASSWORD")
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_DEBUG = False


    #web compress
    COMPRESS_ALGORITHM = 'gzip'
    COMPRESS_MIMETYPES = [
        "text/html", "text/css", "text/xml", "text/plain", "text/svg", 
        "multipart/form-data",
        "application/json", "application/javascript", "application/x-www-form-urlencoded"
    ]
    COMPRESS_LEVEL = 9

    #MySQL config
    SQL_PORT = getenv("SQL_PORT") or "3306"
    SQL_HOST = "127.0.0.1"
    SQL_SCHEMA = getenv('SQL_SCHEMA') or "qickstudy_db"
    SQL_USER = getenv('SQL_USER') or "root"
    SQL_PASSWORD = getenv('SQL_PASSWORD') or "123456"
    SQL_CHARSET = "utf8mb4"
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_SCHEMA}?charset={SQL_CHARSET}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    #Redis config
    REDIS_HOST = getenv("REDIS_HOST") or "127.0.0.1"
    REDIS_PORT = int(getenv("REDIS_PORT") or "6379") 


class debug(Config):
    SECRET_KEY = "QickStudy"
    DEBUG = True

class build(Config):
    #config
    SECRET_KEY = urandom(64).hex()
    DEBUG = False

def getAppMode():
    return getenv("app_mode") or "build";