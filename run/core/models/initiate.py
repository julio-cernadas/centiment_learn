#!/usr/bin/env python3
from core.mappers.Connections import Select, Insert

def logging(username,password):
    user = Select().select_existing_account(username,password)
    return user

def register(first,last,username,password,prev):
    Insert().insert_account(first,last,username,password,prev)

