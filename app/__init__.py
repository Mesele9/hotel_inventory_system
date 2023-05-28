import os
from flask import Flask, render_template, url_for
from config import Config
from flask_migrate import Migrate
from app.dbcon import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    # inittialize database   
    db.init_app(app)


    # initialize migration
    migrate = Migrate(app, db)


    # import all models from Models directory
    from app.models.users import Users
    from app.models.products import Products
    from app.user_bp.form import LoginForm 


    # register blueprints
    from app.user_bp import bp as user_bp
    from app.manage_product_bp import bp as product_bp
    from app.manage_purchase_bp import bp as purchase_bp
    from app.manage_issue_bp import bp as issue_bp
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(product_bp, url_prefix='/product')
    app.register_blueprint(purchase_bp, url_prefix='/purchase')
    app.register_blueprint(issue_bp, url_prefix='/issue')

    @app.route('/')
    def index():
        return render_template('base.html')

    return app


#from app import create_app




