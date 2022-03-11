from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,validators,TextAreaField,SelectField
from flask_login import current_user

from app_blog.blog.model import Blog_Category, Blog_Main
from wtforms.ext.sqlalchemy.fields import QuerySelectField

import wtforms.ext.sqlalchemy.fields as t

class Form_Blog_Main(FlaskForm):
    blog_name=StringField('Blog_Name',validators=[
        validators.DataRequired(),
        validators.Length(1,30)
    ])
    blog_descri=TextAreaField('Blog_Descri',validators=[
        validators.Length(0,300)
    ])
    submit=SubmitField('Create Blog')

def get_category():
    return Blog_Category.query

def get_blog():
    return Blog_Main.query.filter_by(artist=current_user._get_current_object().id)

class Form_Blog_Post(FlaskForm):
    """
    建置blog文章的表單
    """
    post_title = StringField('Post_Title', validators=[
        validators.DataRequired(),
        validators.Length(1, 80)
    ])
    post_body = TextAreaField('Post_Body', validators=[
        validators.DataRequired()
    ])

    post_blog = QuerySelectField('Post_Blog', query_factory=get_blog, get_label='blog_name')
    post_category = QuerySelectField('Post_Category', query_factory=get_category, get_label='name')

    submit = SubmitField('Submit Post')
    def __init__(self):
        super(Form_Blog_Post, self).__init__()
        self.post_blog.choices = self._get_blog_main()
        self.post_category.choices = self._get_category()


    def _get_blog_main(self):
        obj = Blog_Main.query.with_entities(Blog_Main.id, Blog_Main.blog_name).filter_by(artist=current_user._get_current_object().id).all()
        return obj


    def _get_category(self):
        obj = Blog_Category.query.with_entities(Blog_Category.id, Blog_Category.name).all()
        return obj

def get_pk_from_identity(obj):
    cls, key = t.identity_key(instance=obj)[:2]
    return ':'.join(t.text_type(x) for x in key)

t.get_pk_from_identity = get_pk_from_identity