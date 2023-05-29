from flask import Blueprint, jsonify
from flask import render_template, flash, url_for, request, redirect
from app.dbcon import db
from app.manage_users.form import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, current_user, login_required


users_bp = Blueprint('users_bp', __name__, url_prefix='/users')



from app.models.users import Users


@users_bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and (user.password == form.password.data):
            login_user(user)
            flash('You have been logged in successfully', 'success')
            return redirect(url_for('index'))
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
        new_user = Users(name=form.name.data, username=form.username.data, password=form.password.data, role=form.role.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('users_bp.login'))
        
    return render_template('users_auth/add_user.html', title='Add User', form=form)


@users_bp.route('/')
def index():
    user_list = Users.query.all()
    u = []
    for user in user_list:
        u.append(user.username)
    return u
