from dataclasses import dataclass
from datetime import datetime
from tkinter.tix import Form
from flask import render_template,flash,redirect,url_for
from app_blog.decorator_permission import decorator_permission
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
import time
import hashlib
from werkzeug.utils import secure_filename
import os

db.create_all()
@blog.route('/blog_main/c/', methods=['GET', 'POST'])
@login_required
def post_blog_main():
    form=Form_Blog_Main()
    if form.validate_on_submit():
        if form.image_uploads.data :
            f=form.image_uploads.data
            file_name=secure_filename(f.filename)
            f.save(os.path.join("D:/trianning/Bigbang_Fan/app_blog/static/image_folder", file_name))
            file_url="/static/image_folder/"+ file_name
        else:
            file_url=None  
        blog=Blog_Main(
            blog_name=form.blog_name.data,
            blog_descri=form.blog_descri.data,
            artist=current_user.id,
            blog_cover_url=file_url,
        )
        current_user.blog_mains.append(blog)
        db.session.add(blog)
        db.session.commit()
        flash('Create New Blog Success')
        return redirect(url_for('main.userinfo',username=current_user.username))
    return render_template('blog/blog_main_edit.html',form=form)



@blog.route('/blog_post/c', methods=['GET', 'POST'])
@login_required
def post_blog_post():
    form = Form_Blog_Post()

    if form.validate_on_submit():
        post = Blog_Post(
            title=form.post_title.data,
            body=form.post_body.data,
            category=form.post_category.data.id,
            artist=current_user._get_current_object(),
            blog_main=form.post_blog.data.id,
            slug='%i-%i-%i-%i-%s' % (current_user.id, datetime.now().year, datetime.now().month, datetime.now().day,
                                  slugify(form.post_title.data))
        )
        
        db.session.add(post)
        db.session.commit()
        flash('Blog Post Success')
        return redirect(url_for('blog.read_blog_post',slug=post.slug))
    return render_template('blog/blog_post_edit.html', form=form)


@blog.route('/post_list/<blog_id>/')
def post_list(blog_id):
    posts=Blog_Post.query.filter_by(blog_main_id=blog_id).all()
    blog=Blog_Main.query.filter_by(id=blog_id).first_or_404()
    return render_template('blog/blog_post_list.html',posts=posts,blog=blog)


@blog.route('/blog_post/r/<slug>')
@decorator_permission
@login_required
def read_blog_post(slug):
    if not current_user.check_artist('app_blog.blog.view1', 'read_blog_post'):
        flash('You Have No Author!')
        return redirect(url_for('main.index'))
    post=Blog_Post.query.filter_by(slug=slug).first_or_404()
    return render_template('blog/blog_post_read.html',post=post)

@blog.route('/blog_post/u/<int:post_id>/',methods=['GET','POST'])
@login_required
def update_blog_post(post_id):
    post=Blog_Post.query.filter_by(id=post_id).first_or_404()
    form=Form_Blog_Post()
    if form.validate_on_submit():
        post.title = form.post_title.data
        post.body = form.post_body.data
        print(form.post_body.data)
        post.blog_main_id = form.post_blog.data.id
        post.category_id = form.post_category.data.id
        db.session.add(post)
        db.session.commit()
        flash('Edit Your Post Success')
        return redirect(url_for('blog.read_blog_post',slug=post.slug))
    form.post_title.data=post.title
    form.post_body.data=post.body
    form.post_blog.data=post.blog_main_id
    form.post_category.data=post.category_id

    return render_template('blog/blog_post_edit.html',form=form,post=post,action='edit')


@blog.route('/blog_main/u/<int:blog_id>/',methods=['GET','POST'])
@login_required
def update_blog_main(blog_id):
    blog=Blog_Main.query.filter_by(id=blog_id).first_or_404()
    form=Form_Blog_Main()
    if form.validate_on_submit():
        file_url=''
        if not form.image_uploads.data and blog.blog_cover_url:
            file_url=blog.blog_cover_url
        if form.image_uploads.data:
            f=form.image_uploads.data
            file_name=secure_filename(f.filename)
            f.save(os.path.join("D:/trianning/Bigbang_Fan/app_blog/static/image_folder", file_name))
            file_url="/static/image_folder/"+ file_name
        if not file_url:
            file_url = None
        blog.blog_name=form.blog_name.data
        blog.blog_descri=form.blog_descri.data
        blog.blog_cover_url=file_url
        db.session.add(blog)
        db.session.commit()
        flash('Update Blog Main!')
        return redirect(url_for('main.userinfo',username=current_user.username))

    form.blog_name.data=blog.blog_name
    form.blog_descri.data=blog.blog_descri
    form.image_uploads=blog.blog_cover_url
    return render_template('blog/blog_main_edit.html',form=form,action='edit')


@blog.route('/blog_test/')
@decorator_permission
@login_required
def blog_test():
    return 'i am test route'
