#-*- coding: utf-8 -*-
from flask import render_template, flash, redirect, jsonify, session, url_for, g, abort, request
from app import app
from .forms import LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from app import db, models
from .models import User
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug import secure_filename
import json
from subprocess import call
import time
import os
import sys
from pprint import pprint
from app import models

@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    error=None
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = models.User.query.filter_by(username=username).first()
    if registered_user is None:
        error = 'Usuario nao cadastrado'
        return render_template('login.html', error=error)
    if not registered_user.check_password(password):
        error = 'Senha esta incorreta'
        return render_template('login.html', error=error)
    #login_user(registered_user)
    return render_template('teste.html', name=username)

@app.route('/user/<name>')
def user(name):
   return render_template('teste.html', name=name)
