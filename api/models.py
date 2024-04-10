from flask import current_app
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
from . import db

class Table:

    TableArgs = {
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_general_ci'    
    }

class Permission:
    '''
        User's permission class

        [
            0 ,#是否能够登录后台,root
            0 ,#能否修改管理员以下的权限，及决定用户是否能够发布文章、关注他人、账号是否被封禁
            0 ,#能否发布文章
            0 ,#能否关注他人、签到、发布评论
            0 ,#账号是否被封禁或注销
        ]
    '''
    default = [ 0 , 0 , 1 , 1 , 0 ]

    def isRoot(permission:list) -> bool:
        rate = permission[0]
        return (
            bool(rate)
            and
            type(rate) == int
            and
            rate == 1
        )

    def isAdministrator(permission:list) -> bool:
        rate = permission[1]
        return (
            bool(rate)
            and
            type(rate) == int
            and
            rate == 1
        )
    
    def couldPosts(permission:list) -> bool:
        pass
    

    def couldComments(permission:list) -> bool:
        pass;

    def isNormal(permission:list) -> bool:
        pass


class Comments(db.Model):
    pass


class Posts(db.Model):
    pass
    

class Logs(db.Model):
    '''
        log database
    '''
    __tablename__ = 'Qick_logs'
    __table_args__ = Table.TableArgs

    id = db.Column(db.Integer,primary_key = True);
    logTime = db.Column('logTime',db.DateTime(),default=datetime.datetime.now());
    context = db.Column('context',db.Text);
    userid = db.Column('userid',db.Integer,db.ForeignKey('user.id'));
    required = db.Column('required',db.Boolean,default=False,comment="是否已读");

    def __repr__(self) -> str:
        return '<Logs by User %s>' % self.userid
    
            
class User(db.Model):
    '''
        logined by username or email
    '''
    __tablename__ = "Qick_Users"
    __table_args__ = Table.TableArgs

    id = db.Column(db.Integer,primary_key = True);
    username = db.Column('username',db.String(50),unique=True,index=True,comment="用户名可用于登录"); #唯一
    password = db.Column('password',db.String(128));
    email = db.Column('email',db.String(100),unique=True,index=True);
    """
        权限分割
    """
    permission = db.Column('permission')

    #对外展示，可变
    nickname = db.Column('nickname',db.String(50));
    avatar = db.Column('avatar',db.LargeBinary);
    signatureText = db.Column('signatureText',db.String(100)); #个性签名

    #time
    registerTime = db.Column('registerTime',db.DateTime(),default=datetime.datetime.now());
    resetTime = db.Column('resetTime',db.DateTime(),default=datetime.datetime.now());

    #user's log
    logs = db.relationship('Logs',backref = 'user');

    posts = db.relationship('Posts',backref = 'author',lazy = 'dynamic');

    comments = db.relationship('Comments',backref = 'author', lazy = 'dynamic');

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute");

    @password.setter
    def password(self,pwd):
        self.password = generate_password_hash(pwd);

    def isAdministrator(self):
        return Permission.isAdministrator(
            self.permission
        )
    
    def changePermission(self,permission):
        pass
