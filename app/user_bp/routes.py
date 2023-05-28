from flask import render_template, url_for, request, redirect
from app.user_bp import bp
from app.dbcon import db
from app.models.users import Users
from app.user_bp.form import LoginForm

@bp.route('/')
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

@bp.route('/login')
def login():
    form = LoginForm()
    #return 'Login form'
    return render_template(('login.html'), form=form)
