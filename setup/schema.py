#!/usr/bin/env python3
import sqlite3

connection = sqlite3.connect('master.db',check_same_thread=False)
cursor     = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16) UNIQUE,
        password VARCHAR(32),
        first VARCHAR(32),
        last VARCHAR(32),
        prev VARCHAR(8)
    );"""
)

cursor.execute(
    """CREATE TABLE social(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATETIME,
        comment VARCHAR,
        username VARCHAR(16),
            FOREIGN KEY(username) REFERENCES users(username)
    );"""
)

cursor.close()
connection.close()