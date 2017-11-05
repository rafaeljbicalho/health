from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from app import db

class LoginForm(Form):
    name = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
