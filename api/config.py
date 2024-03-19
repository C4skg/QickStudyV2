from os import urandom,getenv

class config:
    #config
    SECRET_KEY = urandom(32)
    DEBUG = False


    #email config
    MAIL_SERVER='smtp.qq.com'
    MAIL_PORT='465'
    MAIL_USERNAME='QickStudy@qq.com'
    MAIL_PASSWORD=''
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False
    MAIL_DEBUG = False


    #web compress
    COMPRESS_ALGORITHM = 'gzip'
    COMPRESS_MIMETYPES = [
        "text/html", "text/css", "text/xml", "text/plain", "text/svg", 
        "image/png","image/jpeg",
        "multipart/form-data",
        "application/json", "application/javascript", "application/x-www-form-urlencoded"
    ]
    COMPRESS_LEVEL = 9

    #MySQL config
    SQL_PORT = "3306"
    SQL_HOST = "127.0.0.1"
    SQL_SCHEMA = getenv('SQL_SCHEMA') or "qickstudy_db"
    SQL_USER = getenv('SQL_USER') or "root"
    SQL_PASSWORD = getenv('SQL_PASSWORD') or "123456"
    SQL_CHARSET = "utf8mb4"
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_SCHEMA}?charset={SQL_CHARSET}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class debug(config):
    SECRET_KEY = "QickStudy"
    DEBUG = True
