from ast import Pass
from django.forms import ValidationError
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,validators,PasswordField
from wtforms.fields.html5 import EmailField
from app_blog.model import Users

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