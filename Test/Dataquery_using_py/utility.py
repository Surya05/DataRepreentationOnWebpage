#!/usr/bin/python
import sqlite3 as db
import sys
def query_db(query,bind_variable=None):
	con = db.connect('chinook.db')
	cur = db.Cursor(con)
	try:
		if bind_variable==None:
			cur.execute(query)
		else:
			cur.execute(query,bind_variable)
		result = cur.fetchall()
		return result
	except:
		print("Oops!",sys.exc_info()[0],"occured.")
	finally:
		cur.close()
		con.commit()
		con.close()	
		print("Connection Closed")