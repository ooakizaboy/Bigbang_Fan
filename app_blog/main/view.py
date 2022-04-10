from django.shortcuts import redirect, render
from flask_login import current_user, login_required
from flask import render_template,redirect,url_for,flash,abort

from app_blog.main.form import FormRole_Func_manager
from . import main
from app_blog.main.form import FormUserInfo
from app_blog import db
from app_blog.artist.model import Users
from app_blog.artist.form import FormFunc,FormRole
from app_blog.artist.model import Func,Role

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

@main.route('/redirectuserinfo',methods=['GET','POST'])
@login_required
def redirectuserinfo():
    return redirect(url_for('main.userinfo',username=current_user.username))

@main.route('/userinfo/<username>')
@login_required
def userinfo(username):
    user=Users.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('main/userinfo.html',user=user)

@main.route('/viewfunction/c/', methods=['GET', 'POST'])
def view_function_c():
    form=FormFunc()
    if form.validate_on_submit():
        func=Func(
            func_module_name=form.func_module_name.data,
            func_description=form.func_description.data,
            func_is_activate=form.func_is_activate.data,
            func_remark=form.func_remark.data
        )
        db.session.add(func)
        db.session.commit()
        flash('New Func %s Register Success...' %form.func_module_name.data)
        return redirect(url_for('main.view_function_c'))
    return render_template('main/createViewFunction.html',form=form)

@main.route('/viewfunction/r/<int:page>/',methods=['GET'])
def view_function_r(page=1):

    columns = ['ID', 'Module_Name', 'Func_Description', 'is_activate' , 'Func_Remark']
    funcs = Func.query.paginate(page, 5, False)
    return render_template('main/readViewFunction.html', funcs=funcs, columns=columns)

@main.route('/viewfunction/e/<int:func_id>/',methods=['GET','POST'])
@login_required
def view_function_e(func_id):
    func=Func.query.filter_by(id=func_id).first_or_404()
    form=FormFunc(obj=func)
    if form.validate_on_submit():
        form.populate_obj(func)
        db.session.commit()
        flash('Update Func Success!')
        return redirect(url_for('main.view_function_r',page=1))
    return render_template('main/createViewFunction.html',form=form)

@main.route('/rolemanager/c/',methods=['GET','POST'])
@login_required
def role_manager_c():
    form=FormRole()
    if form.validate_on_submit():
        role=Role(
            name=form.name.data
        )
        db.session.add(role)
        db.session.commit()
        flash('New Role %s Register Success..' %form.name.data)
        return redirect(url_for('main.role_manager_c'))
    return render_template('main/managerRole.html',form=form,action='create')

@main.route('/rolemanager/r/<int:page>/',methods=['GET'])
@login_required
def role_manager_r(page=1):
    columns=['ID','Role_Name']
    roles=Role.query.paginate(page,10,False)
    return render_template('main/readRole.html',roles=roles,columns=columns)


@main.route('/rolemanager/e/<int:role_id>/',methods=['GET','POST'])
@login_required
def role_manager_e(role_id):
    role=Role.query.filter_by(id=role_id).first_or_404()
    form=FormRole(obj=role)
    if form.validate_on_submit():
        form.populate_obj(role)
        db.session.commit()
        flash('Update Role Success!')
        return redirect(url_for('main.role_manager_r',page=1))
    return render_template('main/managerRole.html',form=form,action="edit")


@main.route('/role_func_manager/<int:role_id>/',methods=['GET','POST'])
def role_func_manager(role_id):
    form=FormRole_Func_manager()
    all_funcs=Func.query.with_entities(Func.id,Func.func_module_name).all()
    form.all_function_option.choices=[(id,role)for id ,role in all_funcs]
    return render_template('main/Role_Func_manager.html',form=form)