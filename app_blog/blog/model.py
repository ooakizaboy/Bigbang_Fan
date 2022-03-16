from unicodedata import category

from numpy import tile
from app_blog import artist
from app_blog import db 
from datetime import datetime




class Blog_Main(db.Model):
    __tablename__="Blog_Main"
    id=db.Column(db.Integer,primary_key=True)
    blog_name=db.Column(db.String(30),nullable=False)
    blog_descri=db.Column(db.String(200))
    blog_create_date=db.Column(db.DateTime,default=datetime.utcnow)
    artist=db.Column(db.Integer,db.ForeignKey('users.id'))
    posts = db.relationship('Blog_Post', backref='blogs', lazy='dynamic')
    blog_cover_url = db.Column(db.String(50))
    


    def __init__(self,blog_name,blog_descri,artist,blog_cover_url):
        self.blog_name=blog_name
        self.blog_descri=blog_descri
        self.artist=artist
        self.blog_cover_url=blog_cover_url

    def __repr__(self):
        return '<blog>:%s, <artist>:%s' %(self.blog_name,self.artist)

class Blog_Category(db.Model):
    __tablename__='Blog_Categorys'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    remark=db.Column(db.String(50))

    def __init__(self,name,remark):
        self.name=name
        self.remark=remark
    def __repr__(self):
        return '<Category> %s' %self.name

class Blog_Post(db.Model):
    __tablename__='Blog_Posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('Blog_Categorys.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_main_id = db.Column(db.Integer, db.ForeignKey('Blog_Main.id'))
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    edit_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    slug = db.Column(db.String(256), unique=True)
    flag = db.Column(db.Boolean, default=True)
    categorys = db.relationship('Blog_Category', backref=db.backref('posts', lazy='dynamic'))


    def __init__(self, title, body, category,artist, blog_main, slug=None):
        self.title = title
        self.body = body
        self.category_id = category
        self.artist_id = artist.id
        self.blog_main_id = blog_main
        self.slug = slug
        

    def __repr__(self):
        return '<POST> %s' % self.title

            