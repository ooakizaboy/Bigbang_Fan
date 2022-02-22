from app_blog import app
from app_blog import db
from flask import render_template
from app_blog.model import Users
from app_blog.form import FormRegister

db.create_all()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    from app_blog.form import FormRegister
    from app_blog.model import Users
    form =FormRegister()
    if form.validate_on_submit():
        user=Users(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        return render_template('home.html',user=user)
    return render_template('register.html',form=form)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/member')
def member():
    return render_template('member.html')

@app.route('/album')
def album():
    return render_template('album.html')


