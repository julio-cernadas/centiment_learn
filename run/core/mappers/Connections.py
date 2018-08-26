#!/usr/bin/env python3
import sqlite3
from core.mappers.Base import Base

# ____________________ SELECTS ____________________ #
class Select(Base):
	def select_existing_account(self,username,password):
		sql_cmd = """SELECT username,password 
					FROM users 
					WHERE username=? AND password=?;"""
		try:
			username = self.connect_fetch(sql_cmd,(username,password,))
			return username
		except IndexError:
			return None

	def select_user_info(self,username):
		sql_cmd =	"""SELECT first,prev
						FROM users
						WHERE username=?;"""
		items = [i for i in self.connect_multi(sql_cmd,(username,))]
		return items

	def select_all_posts(self):
		sql_cmd =	"""SELECT username,date,comment
						FROM social;"""
		items = [i for i in self.connect_to_all(sql_cmd)]
		return items

	def select_all_user_posts(self,username):
		sql_cmd =	"""SELECT username,date,comment
						FROM social
						WHERE username=?;"""
		items = [i for i in self.connect_multi(sql_cmd,(username,))]
		return items

	def select_repost_counter(self,post_ID):
		sql_cmd =	"""SELECT count(*)
						FROM reposts
						WHERE post_ID=?;"""
		count = self.connect_fetch(sql_cmd,(post_ID,))
		return count

	def select_repost_user(self,username):
		sql_cmd =	"""SELECT count(*)
						FROM reposts
						WHERE username=?;"""
		count = self.connect_fetch(sql_cmd,(username,))
		return count

	def select_post_user(self,username):
		sql_cmd =	"""SELECT count(*)
						FROM social
						WHERE username=?;"""
		count = self.connect_fetch(sql_cmd,(username,))
		return count

	def select_repost(self,username,post_ID):
		sql_cmd = """SELECT username
					FROM reposts
					WHERE username=? AND post_ID=?;"""
		try:
			username = self.connect_fetch(sql_cmd,(username,post_ID,))
			return username
		except IndexError:
			return None

# ____________________ INSERTS ____________________ #
class Insert(Base):
	def insert_account(self,first,last,username,password,prev):
		sql_cmd = """INSERT INTO users(
					first, last, username, password, prev) 
					VALUES(?,?,?,?,?);"""
		self.connect(sql_cmd,(first,last,username,password,prev,))
    
	def insert_tweet(self,username,date,comment):
		sql_cmd = """INSERT INTO social(
					username, date, comment) 
					VALUES(?,?,?);"""
		self.connect(sql_cmd,(username,date,comment,))

	def insert_repost(self,username,post_id):
		sql_cmd = """INSERT INTO reposts(
					username, post_ID) 
					VALUES(?,?);"""
		self.connect(sql_cmd,(username,post_id,))

	def insert_repost_user(self,username,count):
		sql_cmd = """UPDATE users
					SET reposts=?
					WHERE username=?;"""
		self.connect(sql_cmd,(count,username,))

	def insert_post_user(self,username,count):
		sql_cmd = """UPDATE users
					SET posts=?
					WHERE username=?;"""
		self.connect(sql_cmd,(count,username,))


# ____________________ DELETES ____________________ #
class Delete(Base):
	def delete_holding(self,ticker,username,type):
		sql_cmd ='''SELECT rowid 
					FROM holdings 
					WHERE ticker="{0}" AND 
					username="{1}" AND
					type='{2}';'''.format(ticker,username,type)
		id = self.connect_fetch(sql_cmd)
		sql_cmd = 'DELETE FROM holdings WHERE rowid={0};'.format(id,)
		self.connect(sql_cmd)