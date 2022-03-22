from urllib import request
import bcrypt
from flask import Flask,render_template,g,request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_babel import Babel,lazy_gettext, gettext, ngettext, refresh

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.abspath(os.path.dirname(__file__))+"\\static\\data\\data_register.db"
app.config['SECRET_KEY']='7894561230'
bootstrap=Bootstrap(app)
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
migrate = Migrate(app, db)
babel=Babel(app)



login=LoginManager(app)
login.login_view='artist.login'

from app_blog.artist import artist
app.register_blueprint(artist, url_prefix='/artist')
from app_blog.main import main
app.register_blueprint(main, url_prefix='/main')
from app_blog.blog import blog
app.register_blueprint(blog, url_prefix='/blog')