#!/usr/bin/env/ python3
from sqlite3 import connect

class Base:
    '''Used for Connections to Database for SQL commands!'''
    def connect(self, sql_cmd, values):
        with connect('master.db', check_same_thread=False) as conn:
            cur = conn.cursor()
            cur.execute(sql_cmd, values)
            conn.commit()
            cur.close()

    def connect_fetch(self, sql_cmd, values):
        with connect('master.db', check_same_thread=False) as conn:
            cur = conn.cursor()
            cur.execute(sql_cmd, values)
            return cur.fetchall()[0][0]

    def connect_list(self, sql_cmd):
        with connect('master.db', check_same_thread=False) as conn:
            cur = conn.cursor()
            cur.execute(sql_cmd)
            return cur.fetchall()[0]
    
    def connect_multi(self, sql_cmd, values):
        with connect('master.db', check_same_thread=False) as conn:
            cur = conn.cursor()
            cur.execute(sql_cmd, values)
            return cur.fetchall()

    def connect_to_all(self, sql_cmd):
        with connect('master.db', check_same_thread=False) as conn:
            cur = conn.cursor()
            cur.execute(sql_cmd)
            return cur.fetchall()
