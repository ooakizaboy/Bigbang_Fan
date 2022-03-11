from pydoc import TextRepr
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,validators,SelectField,TextAreaField

class FormUserInfo(FlaskForm):
    about_me=TextAreaField('About Me',
           validators=[validators.DataRequired()
    ])
    location=StringField('Location',validators=[
        validators.DataRequired(),validators.Length(1,20)
    ])
    gender=SelectField('Gender',validators=[
        validators.DataRequired()
    ],choices=[('F','Female'),('M','Man')])
    submit=SubmitField('Submit UserInfo')

    # def __init__(self):
    #     super(FormUserInfo,self).__init__()
    #     self.gender.choices=[('A','A'),('B','B')]

