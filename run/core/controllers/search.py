#!/usr/bin/env python3
from flask import Blueprint, render_template, request, session, redirect, url_for
from core.models.dashboard import user_info, all_tweets, record_tweet
from core.models.searching import search_api
from core.models.ml_model  import outputs

controller = Blueprint('search',__name__,url_prefix='/search')
	
@controller.route('/',methods=['GET','POST'])
def show_dashboard():
    if request.method == 'GET':
        if 'username' in session:
            search = request.args.get('search')
            lst,ticker = search_api(search.lower())
            username    = session['username']
            information = user_info(username)
            items = all_tweets()
            x, y_pos ,y_price ,y_neg = outputs(ticker)
            return render_template('search.html', username = username,
                    x=x, y_pos=y_pos, y_neg=y_neg, y_price=y_price,
                    information=information, items=items,ticker=ticker,lst=lst)

        elif request.method == 'POST':
            if 'username' in session:
                username = session['username']			
                comment    = request.form['tweet']
                record_tweet(username,comment)
                if comment != None:
                    return redirect(url_for('home.dashboard'))

@controller.route('/',methods=['GET','POST'])
def dashboard():
	return info(session['username'])
