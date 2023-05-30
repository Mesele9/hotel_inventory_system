from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from flask_login import current_user


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remeber Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    name = StringField('Employee Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('', 'Select Role'), ('admin', 'Admin'), ('manager', 'Manager'), ('store_keeper', 'Store Keeper'), ('others', 'Others')], validators=[DataRequired()])
    submit = SubmitField('Add User')


    def validate_username(self, username):
        from app.models.users import Users
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exist. Please choose another')
        

class EditAccountForm(FlaskForm):
    name = StringField('Employee Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    role = SelectField('Role', choices=[('admin', 'Admin'), ('manager', 'Manager'), ('store_keeper', 'Store Keeper'), ('others', 'Others')], validators=[DataRequired()])
    submit = SubmitField('Update User')


    def validate_username(self, username):
        from app.models.users import Users
        if username.data != current_user.username:
            user = Users.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exist. Please choose another')