from functools import wraps
from flask_login import current_user
from flask import flash,redirect,url_for

def decorator_permission(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user._get_current_object().check_artist(func.__module__, func.__name__):
            flash('Good Job')
            return func(*args, **kwargs)
        else:
            flash('you have no author, please fill in IT order!')
            return redirect(url_for('artist.home'))
    return wrapper