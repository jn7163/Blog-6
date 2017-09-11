from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import Email, Length, Required


class LoginForm(FlaskForm):
    email = StringField(
        'Email', validators=[Required(), Length(1, 64),
                             Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
