#!/usr/bin/python
from flask import Flask
from  return_response import *
app = Flask(__name__)

@app.route('/')
def hello():
	return welcome()
	
@app.route('/album/<albumid>')
def album_info(albumid):
	return album_info_using_id(albumid)
	
@app.route('/search/album/<albumname>')
def search_albums_using_album(albumname):
	return search_albums_using_album_name(albumname)
	
@app.route('/search/artist/<artistname>')
def search_albums_using_artist(artistname):
	return search_albums_using_artist_name(artistname)
	
if __name__ == '__main__':
   app.run(debug = True)