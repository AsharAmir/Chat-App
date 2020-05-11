from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

from models import *




def invalid_details(form, field):
    username_entered = form.username.data
    password_entered = field.data

    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError('Username or password is incorrect!')
    elif password_entered != user_object.password:
        raise ValidationError('Username or password is incorrect!')


class Registeration(FlaskForm):
    username = StringField('username_label', 
    validators=[InputRequired(message='Username is required!'),
    Length(min=4, max=24, message='Username must be between 4 to 24 characters!')])
    password = PasswordField('password_label', 
    validators=[InputRequired(message='Password is required!'),
    Length(min=4, max=24, message='Password must be between 4 to 24 characters!')])
    confirm_password = PasswordField('confirm_password',
    validators=[InputRequired(message='Password is required!'),
    EqualTo('password', message='Passwords dont match!')])
    submit_button = SubmitField('Create an account!')


class LoginForm(FlaskForm):
    username = StringField('username_label', validators=[InputRequired(message = 'Username Required.')])
    password = PasswordField('password_label', validators=[InputRequired(message = 'Password Required.'), invalid_details])
    submit_button = SubmitField('Login')
