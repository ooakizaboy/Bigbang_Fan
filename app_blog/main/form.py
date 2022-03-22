from pydoc import TextRepr
from tkinter import Widget
from django.forms import SelectMultiple
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,validators,SelectField,TextAreaField,widgets
from wtforms.fields import SelectMultipleField



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

class MultiCheckField(SelectMultipleField):
    widget=widgets.ListWidget(prefix_label=False)
    option_widget=widgets.CheckboxInput()

class FormRole_Func_manager(FlaskForm):
    all_function_option=MultiCheckField('all_function',coerce=int)
    submit=SubmitField('submit')

