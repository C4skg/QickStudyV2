from flask import current_app

import datetime
from . import db

class Table:
    User = 'Qick_Users'

    TableArgs = {
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_general_ci'    
    }

class User(db.Model):
    __tablename__ = Table.User
    __table_args__ = Table.TableArgs

    id = db.Column(db.Integer,primary_key = True);
    username = db.Column('username',db.String(50),unique=True,index=True); #唯一
    passwordHash = db.Column('password',db.String(128));
    email = db.Column('email',db.String(100),unique=True);

    #对外展示
    nickname = db.Column('nickname',db.String(50));
    avatar = db.Column('avatar',db.String(1000));

    #time
    registerTime = db.Column('registerTime',db.DateTime(),default=datetime.datetime.now())
    resetTime = db.Column('resetTime',db.DateTime(),default=datetime.datetime.now())