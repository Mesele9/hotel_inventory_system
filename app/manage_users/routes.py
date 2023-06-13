from flask import Blueprint
from flask import render_template, flash, url_for, request, redirect
from app.dbcon import db
from app.manage_users.form import LoginForm, RegistrationForm, EditAccountForm
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


# create a blueprint for the users management
users_bp = Blueprint('users_bp', __name__, url_prefix='/users')

from app.models.users import Users


@users_bp.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            flash('Welcome ({})'.format(user.name), 'success')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful, please check your Username or Password', 'danger')
        
    return render_template(('users_auth/login.html'), title='Sign In', form=form)


@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@users_bp.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = Users(name=form.name.data, username=form.username.data,
                         password=generate_password_hash(form.password.data, method='sha256'), role=form.role.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('users_bp.users_list'))
        
    return render_template('users_auth/add_user.html', title='Add User', form=form)


@users_bp.route('/account', methods=('GET', 'POST'))
@login_required
def account():
    form = EditAccountForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.username = form.username.data
        current_user.role = form.role.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users_bp.users_list'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.username.data = current_user.username
        form.role.data = current_user.role

    return render_template('users_auth/account.html', title='Edit User Account', form=form)


@users_bp.route('/')
@login_required
def users_list():
    user_list = Users.query.all()
    return render_template('/users_auth/users_list.html', title='Users List', user_list=user_list)


@users_bp.route('/<int:id>/delete', methods=('GET', 'POST'))
@login_required
def delete_user(id):
    user = db.get_or_404(Users, id)
    if current_user.role != 'admin':
        flash('Action not allowed!', 'danger')
        return redirect(url_for('users_bp.users_list'))
    db.session.delete(user)
    db.session.commit()
    flash('User {} has been deleted!'.format(user.name), 'success')
    return redirect(url_for('users_bp.users_list'))
