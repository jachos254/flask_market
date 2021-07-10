from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField(label='Username:', validators=Length(min=2, max=30))
    email_address = StringField(label='E-mail:')
    password1 = PasswordField(label='Password:', validators=Length(min=6))
    password2 = PasswordField(label='Repeat Password:')
    submit = SubmitField(label='Create Account')