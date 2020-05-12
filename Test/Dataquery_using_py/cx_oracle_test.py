#!/usr/bin/python
import sqlite3 as db
import unicodedata
con = db.connect('chinook.db')
cur = db.Cursor(con)
#cur.execute("INSERT INTO genres(Name) VALUES ('Gangnam Style')");
#cur.execute("UPDATE genres SET Name='Ganjam Style' where GenreId=27");
#print(cur.rowcount)

albumid=65
#cur.execute("select COUNT(*)  from albums a inner join tracks t on a.AlbumId=t.AlbumId where a.AlbumId="+str(a))
#print(cur.fetchone()[0])
#
#cur.execute("select Title from albums where AlbumId="+str(a))
#print(cur.fetchone()[0])
#
#cur.execute("select ar.ArtistId,ar.Name from albums a inner join artists ar on a.ArtistId=ar.ArtistId where a.AlbumId="+str(a))
#for i in cur:
#	print(i[0])
#	print(unicodedata.normalize('NFKD', i[1]).encode('ascii','ignore'))
#
#cur.execute("Select t.TrackId,t.Name,g.Name from albums a inner join artists ar on a.ArtistId=ar.ArtistId inner join tracks t on t.AlbumId=a.AlbumId inner join genres g on t.GenreId=g.GenreId where a.AlbumId="+str(a))
#for i in cur:
#			print(i[0])
#			print(unicodedata.normalize('NFKD', i[1]).encode('ascii','ignore'))
#			print(unicodedata.normalize('NFKD', i[2]).encode('ascii','ignore'))
		

album = {}
cur.execute("select Title from albums where AlbumId="+str(albumid))
#album['album_name']=cur.fetchone()[0]

		
cur.execute("select COUNT(*)  from albums a inner join tracks t on a.AlbumId=t.AlbumId where a.AlbumId="+str(albumid))
album['total_no_of_tracks']=cur.fetchone()[0]
		
album['artist']={}
cur.execute("select ar.ArtistId,ar.Name from albums a inner join artists ar on a.ArtistId=ar.ArtistId where a.AlbumId="+str(albumid))
a = cur.fetchall()
print(a)
print(type(a))
# for i in cur:
# 			album['artist']['id']=i[0]
# 			album['artist']['Name']=unicodedata.normalize('NFKD', i[1]).encode('ascii','ignore')		
# 			
album['songslist']=[]
cur.execute("Select t.TrackId,t.Name,g.Name from albums a inner join artists ar on a.ArtistId=ar.ArtistId inner join tracks t on t.AlbumId=a.AlbumId inner join genres g on t.GenreId=g.GenreId where a.AlbumId="+str(albumid))
# for i in cur:
# 			song = {}
# 			song['id']=i[0]
# 			song['Name']=unicodedata.normalize('NFKD', i[1]).encode('ascii','ignore')
# 			song['genre_name']=unicodedata.normalize('NFKD', i[2]).encode('ascii','ignore')
# 			album['songslist'].append(song)

a = cur.fetchall()
print(a)
print(type(a))
#print(album)
cur.close()
con.commit()
con.close()