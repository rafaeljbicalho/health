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

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    print "NOME:", username
    print "SENHA:", password
    registered_user = models.User.query.filter_by(username=username).first()
    print "AQUI:", registered_user
    if registered_user is None:
        flash('Usuario invalido' , 'error')
        return redirect(url_for('teste'))
    if not registered_user.check_password(password):
        flash('Senha invalida','error')
        return redirect(url_for('login'))
    login_user(registered_user)
    if username == 'timao':
        #flash("Favor trocar sua senha e usuario")
        #return redirect(url_for('register'))
        print "Recebi bicho:", username
    flash('Usuario logado com sucesso')
    #return redirect(request.args.get('next') or url_for('aluno'))
    return render_template('teste.html')

@app.route('/')
@app.route('/index')
def index():
    return "Bem-vindo ao projeto Gym"

@app.route('/instrutor')
def instrutor():
    return "Página do instrutor"

@app.route('/teste')
def teste():
    user = {'nickname': 'Teste'}  # fake user
    return render_template('teste.html',
                           title='bicalho',
                           user=user)
@app.route('/post')
def posts():
    user = {'nickname': 'Bicalho'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("teste.html",
                           title='Posts',
                           user=user,
                           posts=posts)
