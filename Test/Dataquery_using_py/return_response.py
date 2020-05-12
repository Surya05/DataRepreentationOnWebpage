#!/usr/bin/python
from flask import Flask,Response,render_template
from flask import json
import unicodedata
import sys
from utility import *
import traceback

def welcome():
	return render_template('welcome.html')

def album_info_using_id(albumid):
	try:
		album = {}
		query="select Title from albums where AlbumId="+str(albumid)
		query_result=query_db(query)
		if(len(query_result)==0):	
			return("!! Sorry, ! No Matching Found !!")
		else:
			album['album_name']=unicodedata.normalize('NFKD', query_result[0][0]).encode('ascii','ignore')
			album['album_id']=int(albumid)
		
			query="select COUNT(*)  from albums a inner join tracks t on a.AlbumId=t.AlbumId where a.AlbumId="+str(albumid)
			query_result=query_db(query)
			album['total_no_of_tracks']=query_result[0][0]
		
			album['artist']={}
			query="select ar.ArtistId,ar.Name from albums a inner join artists ar on a.ArtistId=ar.ArtistId where a.AlbumId="+str(albumid)
			query_result=query_db(query)
			for i in query_result:
				album['artist']['artist_id']=i[0]
				album['artist']['artist_Name']=unicodedata.normalize('NFKD', i[1]).encode('ascii','ignore')		
			
			album['songslist']=[]
			query="Select t.TrackId,t.Name,g.Name from albums a inner join artists ar on a.ArtistId=ar.ArtistId inner join tracks t on t.AlbumId=a.AlbumId inner join genres g on t.GenreId=g.GenreId where a.AlbumId="+str(albumid)
			query_result=query_db(query)
			for i in query_result:
				song = {}
				song['Track_Id']=i[0]
				song['Track_Name']=unicodedata.normalize('NFKD', i[1]).encode('ascii','ignore')
				song['genre_name']=unicodedata.normalize('NFKD', i[2]).encode('ascii','ignore')
				album['songslist'].append(song)
			print(album)
			print(len(album))
		#album=json.dumps(album)
			return render_template('index.html',album=album)
		#return Response(album,status=200,mimetype="application/json")
	except Exception as err:
		print(traceback.print_exc(err))
		print("Oops!",sys.exc_info()[0],"occured.")
		response = Response("Sorry something wrong has occured",status=500)
		return response

def search_albums_using_album_name(albumname):
	try:
		b=albumname
		a=('%'+b+'%',)
		album = {}
		album['albums']=[]
		query="select a.AlbumId,a.Title,ar.ArtistId,Name from albums a inner join artists ar on a.ArtistId=ar.ArtistId where Title LIKE ?"
		query_result=query_db(query,a)
		if(len(query_result)==0):	
			return("!! Sorry, ! No Matching Found !!")
		else:
			for i in query_result:
				info = {}
				info['Album_Id']=i[0]
				info['Album_Name']=unicodedata.normalize('NFKD', i[1]).encode('ascii','ignore')
				info['Artist']={}
				info['Artist']['id']=i[2]
				info['Artist']['name']=unicodedata.normalize('NFKD', i[3]).encode('ascii','ignore')
				album['albums'].append(info)
		#album=json.dumps(album)	
			return render_template('albuminfo.html',albums=album['albums'])
		#return Response(album,status=200,mimetype="application/json")
	except :
		print("Oops!",sys.exc_info()[0],"occured.")
		response = Response("Some error occured",status=500)
		return response		
		
def search_albums_using_artist_name(artistname):
	try:
		b=artistname
		a=('%'+b+'%',)
		album = {}
		album['albums']=[]
		query="select a.AlbumId,a.Title,ar.ArtistId,Name from albums a inner join artists ar on a.ArtistId=ar.ArtistId where Name LIKE ?"
		query_result=query_db(query,a)
		if(len(query_result)==0):	
			return("!! Sorry, ! No Matching Found !!")
		else:
			for i in query_result:
				info = {}
				info['Album_Id']=i[0]
				info['Album_Name']=unicodedata.normalize('NFKD', i[1]).encode('ascii','ignore')
				info['Artist']={}
				info['Artist']['id']=i[2]
				info['Artist']['name']=unicodedata.normalize('NFKD', i[3]).encode('ascii','ignore')
				album['albums'].append(info)
			print(album)
		#album=json.dumps(album)
			return render_template('albuminfo.html',albums=album['albums'])
		#return Response(album,status=200,mimetype="application/json")
	except :
		print("Oops!",sys.exc_info()[0],"occured.")
		response = Response("Some error occured",status=500)
		return response
