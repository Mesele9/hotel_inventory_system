from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError
#from app.models.users import Users

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
            raise ValidationError('That username already exist, please choose another')