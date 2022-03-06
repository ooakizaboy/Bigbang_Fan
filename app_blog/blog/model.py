from app_blog import db 
from datetime import datetime




class Blog_Main(db.Model):
    __tablename__="BlogMains"
    id=db.Column(db.Integer,primary_key=True)
    blog_name=db.Column(db.String(30),nullable=False)
    blog_descri=db.Column(db.String(200))
    blog_create_date=db.Column(db.DateTime,default=datetime.nctnow)
    author=db.Column(db.Integer,db.ForeignKey('Users.id'))

    def __init__(self,blog_name,blog_descri,author):
        self.blog_name=blog_name
        self.blog_descri=blog_descri
        self.author=author

    def __repr__(self):
        return '<blog>:%s, <author>:%s' %(self.blog_name,self.author)