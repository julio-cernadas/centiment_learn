#!/usr/bin/env python3

from flask import Blueprint, render_template, request, session, redirect, url_for
from core.models.dashboard import user_info, user_tweets, record_tweet

controller = Blueprint('user',__name__,url_prefix='/user')

def info(username):
    if request.method == 'GET':
        if 'username' in session:
            username    = session['username']
            information = user_info(username)
            items = user_tweets(username)
            return render_template('user.html',username = username,
                                    information=information,items=items)

    elif request.method == 'POST':
        if 'username' in session:
            username = session['username']			
            comment  = request.form['tweet']
            record_tweet(username,comment)
            if comment != None:
                return redirect(url_for('user.dashboard'))

@controller.route('/',methods=['GET','POST'])
def dashboard():
    return info(session['username'])
