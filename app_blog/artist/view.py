from django.shortcuts import render
from . import artist
from app_blog import app
from app_blog import db
from flask import render_template,flash,redirect,url_for,request
from app_blog.artist.model import Users
from app_blog.artist.form import FormRegister,FormLogin
from flask_login import login_user,current_user,login_required,logout_user

db.create_all()
@app.route('/')
def index():
    return render_template('index.html')

@artist.route('/register',methods=['GET','POST'])
def register():
    from app_blog.artist.form import FormRegister
    from app_blog.artist.model import Users
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

@artist.route('/home')
@login_required
def home():
    return render_template('home.html')

@artist.route('/login',methods=['GET','POST'])
def login():
    form=FormLogin()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user,form.remember_me.data)
                next=request.args.get('next')
                if not next_is_valid(next):
                    return 'bad'
                return redirect(next or url_for('artist.home',user=current_user.username))
            else:
                flash("worng email or password")
        else:
            flash("worng email or password")

    return render_template('login.html',form=form)
 

@artist.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Log Out See U.')
    return redirect(url_for('artist.login'))

@artist.route('/member')
def member():
    return render_template('member.html')

@artist.route('/album')
def album():
    return render_template('album.html')

@artist.route('/test')
def test():
    return render_template('base.html')


def next_is_valid(url):
    """
    為了避免被重新定向的url攻擊，必需先確認該名使用者是否有相關的權限，
    舉例來說，如果使用者調用了一個刪除所有資料的uri，那就GG了，是吧 。
    :param url: 重新定向的網址
    :return: boolean
    """
    return True


