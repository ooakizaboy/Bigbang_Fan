import bcrypt
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
from flask_bcrypt import Bcrypt 
 
app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.abspath(os.path.dirname(__file__))+"\\static\\data_register.db"
app.config['SECRET_KEY']='7894561230'
bootstrap=Bootstrap(app)
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

from app_blog import view