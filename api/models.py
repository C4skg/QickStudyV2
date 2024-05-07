from flask import current_app
from flask_login import UserMixin,AnonymousUserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from os import urandom

from . import db,loginManager

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
    

class Stars(db.Model):
    __tablename__ = 'Qc_poststars';
    id = db.Column(db.Integer,primary_key=True);
    time = db.Column(db.DateTime(),default=datetime.now()); #点赞时间
    '''
        @ForeignKey
    '''
    userid = db.Column('userid',db.Integer,db.ForeignKey('Qc_Users.id'));
    postsid = db.Column('postsid',db.Integer,db.ForeignKey('Qc_posts.id'));


class Comments(db.Model):
    __tablename__ = "Qc_comment"
    id = db.Column(db.Integer,primary_key=True)
    parentid = db.Column(db.Integer,default=-1); #if id is -1 ,so this comment is the parent comment;
                                                 #else this is the child comment;
    context = db.Column(db.Text);
    disabled = db.Column(db.Boolean);
    time = db.Column(db.DateTime(),default=datetime.now())

    '''
        @ForeignKey
    '''
    userid = db.Column('userid',db.Integer,db.ForeignKey('Qc_Users.id'));
    postsid = db.Column('postsid',db.Integer,db.ForeignKey('Qc_posts.id'));


class PostStatus:
    INVALID = 0;   #被退回
    DRAFT   = 1;   #草稿状态
    WAIT    = 2;   #等待审核状态
    NORMAL  = 3;   #正常发布
    PRIVATE = 4;   #私有状态

class Posts(db.Model):
    __tablename__ = "Qc_posts"
    __table_args__ = Table.TableArgs

    id = db.Column(db.Integer,primary_key=True);
    title = db.Column(db.Text,nullable=False);
    context = db.Column(db.Text,nullable=False);
    cover = db.Column(db.Text,nullable=True); #文章封面路径
    status = db.Column(db.Integer,nullable=False,default=PostStatus.DRAFT,index=True);
    lastmodifytime = db.Column(db.DateTime(),default=datetime.now());
    createtime = db.Column(db.DateTime(),default=datetime.now());

    '''
        @ForeignKey
    '''
    userId = db.Column('userid',db.Integer,db.ForeignKey('Qc_Users.id'));

    '''
        @Relationship
    '''
    comments = db.relationship('Comments',backref = 'posts',lazy = 'dynamic');
    collection = db.relationship('PostsCollection',backref = 'posts',lazy = 'dynamic');
    stars = db.relationship('Stars',backref = 'posts',lazy = 'dynamic');


class PostsCollection(db.Model):
    __tablename__ = 'Qc_postscollection'
    id = db.Column(db.Integer,primary_key=True);
    time = db.Column(db.DateTime(),default=datetime.now());  #收藏时间

    '''
        @ForeignKey
    '''
    userid = db.Column('userid',db.Integer,db.ForeignKey('Qc_Users.id'));
    postsid = db.Column('postsid',db.Integer,db.ForeignKey('Qc_posts.id'));


class Logs(db.Model):
    '''
        log database
    '''
    __tablename__ = 'Qc_logs'
    __table_args__ = Table.TableArgs

    id = db.Column(db.Integer,primary_key = True);
    logTime = db.Column('logTime',db.DateTime(),default=datetime.now());
    context = db.Column('context',db.Text);
    required = db.Column('required',db.Boolean,default=False,comment="是否已读");

    '''
        @ForeignKey
    '''
    userid = db.Column('userid',db.Integer,db.ForeignKey('Qc_Users.id'));


    def __repr__(self) -> str:
        return '<Logs by User %s>' % self.userid
    
            
class User(db.Model):
    '''
        logined by username or email
    '''
    __tablename__ = "Qc_Users"
    __table_args__ = Table.TableArgs

    id = db.Column(db.Integer,primary_key = True);
    username = db.Column('username',db.String(50),unique=True,comment="用户名可用于登录"); #唯一
    password_hash = db.Column('password',db.String(128));
    email = db.Column('email',db.String(100),unique=True,index=True);

    permission = db.Column('permission',db.JSON,nullable=False); #权限，JSON数据

    #对外展示，可变
    nickname = db.Column('nickname',db.String(50),);
    avatar = db.Column('avatar',db.LargeBinary,nullable = True);
    signatureText = db.Column('signatureText',db.String(100),nullable = True); #个性签名

    #time
    registerTime = db.Column('registerTime',db.DateTime(),default=datetime.now());
    resetTime = db.Column('resetTime',db.DateTime(),default=datetime.now());

    #user's log
    logs = db.relationship('Logs',backref = 'user',lazy = 'dynamic');

    posts = db.relationship('Posts',backref = 'user',lazy = 'dynamic');

    comments = db.relationship('Comments',backref = 'user', lazy = 'dynamic');
    
    collection = db.relationship('PostsCollection',backref = 'user',lazy = 'dynamic');

    stars = db.relationship('Stars',backref = 'user',lazy = 'dynamic');


    @property
    def password(self):
        raise AttributeError("password is not a readable attribute");

    @password.setter
    def password(self,pwd):
        self.password_hash = generate_password_hash(pwd);
    
    # @permission.setter
    # def permission(self,value):
    #     if type(value) != str:
    #         pass
    
    def verifyPassword(self,pwd):
        return check_password_hash(self.password,pwd);

    def isAdministrator(self):
        return Permission.isAdministrator(
            self.permission
        )
    
    def changePermission(self,permission):
        pass

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id));


class AnonymousUser(AnonymousUserMixin):
    def can(self,permission):
        return False;

    def isAdministrator(self):
        return False;

loginManager.anonymous_user = AnonymousUser;


# init
def insertAdmin():
    print('starts')
    admin = User.query.filter_by(username='admin').first()
    if admin:
        print("admin user has been exists")
        return;

    password = urandom(4).hex();
    email = input('Set the admin email :').strip();
    admin = User(
        username = 'admin',
        password = password,
        email = email,
        permission = {'1': '1'}
    )
    db.session.add(admin)
    db.session.commit();
    print('admin user info:')
    print('username:','admin')
    print('password:',password)
    print('email   :',email)