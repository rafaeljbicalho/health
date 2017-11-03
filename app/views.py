#-*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)

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
