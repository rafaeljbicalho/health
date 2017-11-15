#-*- coding: utf-8 -*-
from flask import render_template, flash, redirect, jsonify, session, url_for, g, abort, request
from app import app
from .forms import LoginForm, RegistrationForm
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

@app.route('/login')
@app.route('/', methods=['GET','POST'])
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

@app.route('/cadastro', methods=['GET', 'POST'])
def register():
    user = None
    if request.method == 'GET':
        return render_template('cadastro.html')
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        cpf1      = request.form['cpf']
        sexo1     = request.form['sexo']
        data_nascimento1 = request.form['data_nascimento']
        peso1     = request.form['peso']
        altura1     = request.form['altura']
        # print "usuario", nome
        # print "senha", senha
        # print "cpf", cpf1
        # print "sexo", sexo1
        # print "nascimento", data_nascimento1
        # print "peso", peso1
        # print "altura", altura1
        user = models.User(username=nome,password=senha,cpf=cpf1,sexo=sexo1,data_nascimento=data_nascimento1,
                           peso=peso1,altura=altura1)
        print "user:", user
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
