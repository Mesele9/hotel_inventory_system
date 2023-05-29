from flask import Blueprint
from flask import render_template, flash, url_for, request, redirect
from app.dbcon import db
from app.models.users import Users
from app.manage_users.form import LoginForm, RegistrationForm


users_bp = Blueprint('users_bp', __name__, url_prefix='/users')


@users_bp.route('/')
def index():
    return 'user index'
    return render_template('login.html')
    # user = db.session.execute(db.select(Users).order_by(Users.username)).scalars()
    # uli = []
    # for u in user:
    #     uli.append(u.name)
    # return uli

    #return "<h1>This is from User Blueprint</h1>"
    #return render_template(url_for('user.html'))

@users_bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'admin':
            flash('You have been logged in successfully', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful, please check your Username or Password', 'danger')
        
    return render_template(('users_auth/login.html'), title='Sign In', form=form)

@users_bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('users_bp.login'))
        
    return render_template('users_auth/add_user.html', title='Add User', form=form)