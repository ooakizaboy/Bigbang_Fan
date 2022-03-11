from dataclasses import dataclass
from datetime import datetime
from tkinter.tix import Form
from flask import render_template,flash,redirect,url_for
from app_blog.artist.model import Users
from app_blog import artist
from app_blog.blog.form import Form_Blog_Main
from app_blog.blog.model import Blog_Main
from app_blog import db
from flask_login import login_required,current_user
from .import blog
from app_blog.blog.form import Form_Blog_Main,Form_Blog_Post
from app_blog.blog.model import Blog_Main,Blog_Post
from slugify import slugify

db.create_all()

@blog.route('/blog_main/c',methods=['GET', 'POST'])
@login_required
def post_blog_main():
    form=Form_Blog_Main()
    if form.validate_on_submit():
        blog=Blog_Main(
            blog_name=form.blog_name.data,
            blog_descri=form.blog_descri.data,
            artist=current_user.id
        )
        current_user.blog_mains.append(blog)
        db.session.add(current_user)
        db.session.commit()
        flash('Create New Blog Success')
        return redirect(url_for('main.userinfo',username=current_user.username))
    return render_template('blog/blogbook_edit.html',form=form)



@blog.route('/blog_post/c', methods=['GET', 'POST'])
@login_required
def post_blog_post():
    form = Form_Blog_Post()

    if form.validate_on_submit():
        post = Blog_Post(
            title=form.post_title.data,
            body=form.post_body.data,
            category=1,
            artist=current_user._get_current_object(),
            blog_main=form.post_blog.data
            
        )
        db.session.add(post)
        db.session.commit()
        flash('Blog Post Success')
        return redirect(url_for('blog.post_blog_post'))
    return render_template('blog/blog_post_edit.html', form=form)
