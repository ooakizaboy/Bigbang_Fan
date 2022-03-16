from app_blog import db,bcrypt,login
from flask_login import UserMixin
from datetime import datetime

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

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute~')
    
    @password.setter
    def password(self,password):
        self.password_hash=bcrypt.generate_password_hash(password).decode('UTF-8')
    
    def check_password(self,password):
        return bcrypt.check_password_hash(self.password_hash,password)

        
    def __repr__(self):
        return "username:%s, email:%s"%(self.username,self.email)

@login.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
