#!/usr/bin/env python3
from flask import Blueprint, render_template, request, redirect, url_for, session

from core.models.initiate import logging, register

controller = Blueprint('logout',__name__,url_prefix='/logout')

@controller.route('/',methods=['GET'])
def logout():
    if request.method == 'GET':
        session.pop('username',None)
        return redirect(url_for('index.login'))

