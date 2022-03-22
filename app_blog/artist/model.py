from app_blog import db,bcrypt,login
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import text 


relations_user_role=db.Table('relation_user_role',
                                db.Column('user_id',db.Integer,db.ForeignKey('users.id')),
                                db.Column('role_id',db.Integer,db.ForeignKey('roles.id')))

relations_role_func=db.Table('relations_role_func',
                                db.Column('func_id',db.Integer,db.ForeignKey('funcs.id')),
                                db.Column('role_id',db.Integer,db.ForeignKey('roles.id')))


class Users(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    email=db.Column(db.String(80),unique=True,nullable=False)
    password_hash=db.Column(db.String(50),nullable=False)
    about_me=db.Column(db.Text())
    location=db.Column(db.String(20))
    gender = db.Column(db.String(20))
    regist_date=db.Column(db.DateTime(),default=datetime.utcnow())
    last_login=db.Column(db.DateTime(),default=datetime.utcnow())
    blog_mains=db.relationship('Blog_Main',backref='user',lazy='dynamic')
    blog_posts=db.relationship('Blog_Post',backref='user',lazy='dynamic')

    roles=db.relationship('Role',secondary=relations_user_role, lazy='subquery',
                            backref=db.backref('users',lazy=True))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute~')
    
    @password.setter
    def password(self,password):
        self.password_hash=bcrypt.generate_password_hash(password).decode('UTF-8')
    
    def check_password(self,password):
        return bcrypt.check_password_hash(self.password_hash,password)
        
    @property
    def user_func(self):
        func_list=Func.query.join(relations_role_func)\
                      .join(Role)\
                      .join(relations_user_role)\
                      .join(Users)\
                      .filter(Users.id==self.id)
        return func_list
    def check_artist(self,func_module,func_name):
        func_list=self.user_func
        view_function=func_module+'.'+func_name
        result =func_list.filter(text('func_module_name=:view_function'))\
                                .params(view_function=view_function).first()
        if result:
            return True
        else:
            return False
        
    def __repr__(self):
        return "username:%s, email:%s"%(self.username,self.email)


@login.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))



class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))

    funcs=db.relationship('Func',secondary=relations_role_func,lazy='subquery',
                            backref=db.backref('roles',lazy=True))
    
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'Role is %s'%self.name



class Func(db.Model):
    __tablename__='funcs'
    id=db.Column(db.Integer,primary_key=True)
    func_module_name=db.Column(db.String(50))
    func_description=db.Column(db.String(100))
    func_is_activate=db.Column(db.Boolean)
    func_remark=db.Column(db.String(100))

    def __init__(self, func_module_name, func_description, func_is_activate=True, func_remark=None):
        self.func_module_name = func_module_name
        self.func_description = func_description
        self.func_is_activate = func_is_activate
        self.func_remark = func_remark

    def __repr__(self):
        return 'module_name = %s, is_activate = %s' %(self.func_module_name,self.func_is_activate)