from ast import Pass
from email.mime import message
from pickle import TRUE
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,validators,PasswordField,BooleanField,ValidationError
from wtforms.fields.html5 import EmailField
from app_blog.artist.model import Users

class FormRegister(FlaskForm):
    username=StringField('Username',validators=[
        validators.DataRequired(),
        validators.Length(10,30)
        ])
  
    email=EmailField('Email',validators=[
        validators.DataRequired(),
        validators.Length(1,50),
        validators.Email()
    ])

    password=PasswordField('Password',validators=[
        validators.DataRequired(),
        validators.Length(5,10),
        validators.EqualTo('password2',message='PASSWORD NEED MATCH')
    ])

    password2=PasswordField('Confirm password',validators=[
        validators.DataRequired()
    ])
    
    submit=SubmitField('Register New Account')

    def validate_email(self,field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('Email Already Registered By Somebody')
    def validate_username(self,field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('Username Already Registered By Somebody')

class FormLogin(FlaskForm):
    email=EmailField('Email',validators=[
        validators.DataRequired(),
        validators.Length(5,30),
        validators.Email()
    ])

    password=PasswordField('Password',validators=[
        validators.DataRequired()
    ])

    remember_me = BooleanField('keep logged in')

    submit=SubmitField('Log in')

class FormFunc(FlaskForm):
    func_module_name=StringField('func_module_name',validators=[
        validators.DataRequired(),
        validators.Length(max=50,message='Max Length equal 50')
    ])
    func_description=StringField('func_dexcription',validators=[
        validators.DataRequired(),
        validators.Length(max=100,message='Max Length equal 100')
    ])
    func_is_activate = BooleanField('is_activate', validators=[validators.DataRequired(), ],default=True)
    func_remark=StringField('func_remark',validators=[
        validators.DataRequired(),
        validators.Length(max=100,message='Max Length equal 100')
    ])
    submit=SubmitField('Add New View Function')

class FormRole(FlaskForm):
    name=StringField('role_name',validators=[
        validators.DataRequired(),
        validators.Length(max=50,message='Max Length equal 50')
    ])
    submit=SubmitField('Add New Role')

