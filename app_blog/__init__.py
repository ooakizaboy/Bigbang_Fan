import bcrypt
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage



app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.abspath(os.path.dirname(__file__))+"\\static\\data\\data_register.db"
app.config['SECRET_KEY']='7894561230'
bootstrap=Bootstrap(app)
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
migrate = Migrate(app, db)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER ='D:\trianning\Bigbang_Fan\app_blog\static\image_folder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

login=LoginManager(app)
login.login_view='artist.login'



from app_blog.artist import artist
app.register_blueprint(artist, url_prefix='/artist')
from app_blog.main import main
app.register_blueprint(main, url_prefix='/main')
from app_blog.blog import blog
app.register_blueprint(blog, url_prefix='/blog')