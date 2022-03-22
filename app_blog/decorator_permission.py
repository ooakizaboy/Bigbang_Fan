from functools import wraps
from django.shortcuts import redirect
from flask_login import current_user
from flask import flash,url_for

def decorator_permission(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if current_user._get_current_object().check_artist(func.__module__,func.__name__):
            flash('Good Job')
            return func(*args,**kwargs)
        else:
            flash('you have no artist,please fill in IT order!')
            return redirect(url_for('main.index'))
    return wrapper

@decorator_permission
def test_decorator():
    print('test')
