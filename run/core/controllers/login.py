#!/usr/bin/env python3
from flask import Blueprint, render_template, request, redirect, url_for, session

from core.models.initiate import logging, register

controller = Blueprint('index',__name__,url_prefix='')

@controller.route('/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = logging(username,password)
        if user != None:
            session['username'] = username
            return redirect(url_for('home.dashboard'))
        else:
            return render_template('login.html')

@controller.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        first    = request.form['first']
        last     = request.form['last']
        username = request.form['username']
        password = request.form['password']
        register(first,last,username,password,'aapl')
        return redirect('/')
