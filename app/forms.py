# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms.validators import DataRequired
from app import db
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField

class LoginForm(Form):
    name = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

class ZonaForm(Form):
    zonaTipo = SelectField(choices=[("Atividade moderada","Atividade moderada"),("Controle de peso","Controle de peso"),
                                    ("Aerobica","Aerobica"),("Limiar Anaerobica","Limiar Anaerobica"),
                                    ("Esforco maximo","Esforco maximo")])
