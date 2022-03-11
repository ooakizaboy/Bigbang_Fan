from django.shortcuts import redirect
from flask_login import current_user, login_required
from flask import render_template,redirect,url_for,flash,abort
from . import main
from app_blog.main.form import FormUserInfo
from app_blog import db
from app_blog.artist.model import Users

@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('index.html')



@main.route('/edituserinfo',methods=['GET','POST'])
@login_required
def edituserinfo():
    form=FormUserInfo()
    if form.validate_on_submit():
        current_user.about_me=form.about_me.data
        current_user.location=form.location.data
        current_user.gender=form.gender.data
        db.session.add(current_user)
        db.session.commit()
        flash('You Have Already Edit Your Info')
        return redirect(url_for('main.userinfo',username=current_user.username))
    form.about_me.data=current_user.about_me
    form.location.data=current_user.location
    form.gender.data=current_user.gender
    return render_template('main/editUserInfo.html',form=form)

@main.route('/userinfo/<username>')
@login_required
def userinfo(username):
    user=Users.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('main/userinfo.html',user=user)

