# ex1: classroom code(conversion to us floor)
# inp = raw_input('Europe flooer?')
# usf = int(inp) + 1
# print 'US floor', usf

# ex2: test of function
# def product(a, b):
#     c = a * b
#     return c
# a = product(3,5)
# print a
# 
# print type(a)
# 
# print (str(a)+' '+str(a)+'\n')*5

# ex3: test of not-working statement
# def stuff():
#         print 'Hello'
#         return
#         print 'World'
# stuff()

# ex4: assignment 4.6 computepay
# def computepay(h,r):
#   if h < 40:
#        pay = h * r
#   else:
#       pay = (h - 40) * r * 1.5 + 40 * r 
#   return pay
#
# hrs = float(raw_input("Enter Hours:"))
# rate = float(raw_input("Enter Rate:"))
# p = computepay(hrs, rate)
# print p

# ex5: test the break statement
# while True:
#     line = raw_input('> ')
#     if line == 'done':
#         break
#     print line
# print 'Done!'
#
# ex6: average number
# count = 0
# sum = 0
# while True:
#     int = raw_input('Enter a number: ')
#     if int == 'done':
#         break
#     try:
#         int = float(int)
#     except:
#         print 'Invalid input'
#         continue
#     count = count + 1
#     sum = sum + int
#     avg = sum / count
# print 'count:', count, '\n'
# print 'sum:', sum, '\n'
# print 'average', avg, '\n'

# ex7: find the largest and smallest number
# largest = None
# smallest = None
# while True:
#     num = raw_input("Enter a number: ")
#     if num == 'done': break
#     try:
#         num = int(num)
#     except:
#         print 'Invalid input'
#         continue
#     if smallest == None or num < smallest: 
#         smallest = num
#     if largest == None or num > largest:
#         largest = num
# print 'Maximum', largest
# print 'Minimum', smallest

# ex8: average the floating number in a file
# fname = raw_input('Enter file name:')
# fh = open(fname)
# count = 0
# total = 0
# for line in fh:
#     if not line.startswith('X-DSPAM-Confidence:'):
#         continue
#     start = line.find(':')
#     catch = float(line[start+1:])
#     count = count + 1
#     total = total + catch
#     avg = total / count
# print count, total, avg

# ex9: split the words and append to the wordlist (assignment 8.4)
# fname = raw_input('Enter file name:')
# if len(fname) == 0:
#     fname = 'romeo.txt'
# fh = open(fname)
# lst = list()
# for line in fh:
#     sp = line.split()
#     for word in sp:
#         if word not in lst:
#             lst.append(word)    
# lst.sort()
# print lst


# ex10: parsing the text(look for the email address) assignment 8.5
# fname = raw_input('Enter file name:')
# if len(fname) < 1: fname = 'mbox-short.txt'
# fh = open(fname)
# count = 0
# for line in fh:
#     if not line.startswith('From:') and line.startswith('From'):
#         sp = line.split()
#         print sp[1]
#         count = count + 1
# print 'There were', str(count), 'lines in the file with From as the first word'

# ex11: test of get function
# word = 'brontosaurus'
# d = dict()
# for c in word:
#     d[c] = d.get(c,0) + 1
# print d

# ex12: test of importing library - string
# import string
# fname = raw_input('Enter the file name:')
# if len(fname) == 0:
#     fname = 'mbox-short.txt'
# try:
#     fhand = open(fname)
# except:
#     print 'File cannot be opened:', fname
#     exit()
# counts = dict()
# for line in fhand:
#     line = line.translate(None, string.punctuation)
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
# bigword = None
# bigcount = None
# for w, num in counts.items():
#     if bigword == None or num > bigcount:
#         bigword = w
#         bigcount = num
#         print w, num, 'bigword:', bigword, 'bigcount:', bigcount
# print 'Final', bigword, bigcount

# ex 13: find out max from file (assignment 9.4)
# name = raw_input('Enter file:')
# if len(name) < 1:
#     name = 'mbox-short.txt'
# fp = open(name, 'r')
# count = {}
# for line in fp:
#     line = line.strip()
#     if not line.startswith('From:') and line.startswith('From'):
#         s = line.split()
#         if len(s) < 1:
#             continue
#         sender = s[1]
#         count[sender] = count.get(sender, 0) + 1
# 
# max_count = max(count.values())
# for email in count:
#     num = count[email]
#     if num == max_count:
#         print email, num

# ex 14: assignment 10.2 count the hour from mbox-short.txt
# name = raw_input('Enter File name:')
# if len(name) < 1:
#     name = 'mbox-short.txt'
# fp = open(name)
# counts = {}
# for line in fp:
#     line = line.strip()
#     if not line.startswith('From:') and line.startswith('From'):
#         s = line.split()
#         sp = s[5].split(':')
#         hour = sp[0]
#         counts[hour] = counts.get(hour, 0) + 1
# r = counts.items()
# r.sort()
# for key, value in r:
#     print key, value

# ex 15: test of urllib
# import urllib
# fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
# for line in fhand:
#     print line.strip()

# ex 16: test of parsing number from online txt file
# import urllib
# import re
# fhand = urllib.urlopen('http://python-data.dr-chuck.net/regex_sum_305830.txt')
# numlist = []
# for line in fhand:
#     l = re.findall('[0-9]+', line)
#     for n in l:
#         numlist.append(int(n))
# y = sum(numlist)
# print 'Numlist = ', numlist
# print 'Sum:', y

# ex17: an HTTP request in Python(Chapter 12(1)Assignment)
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.pythonlearn.com', 80))
# mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')
# while True:
#     data = mysock.recv(512)
#     if ( len(data) < 1 ) :
#         break
#     print data
# mysock.close()

# ex18: to calculate the sum  on the webpage 
# import urllib
# from BeautifulSoup import BeautifulSoup
# url = raw_input('Enter - ')
# if len(url) == 0:
#     url = 'http://python-data.dr-chuck.net/comments_305835.html'
# html = urllib.urlopen(url).read()
# soup = BeautifulSoup(html)
# # Retrieve all of the anchor tags
# tags = soup('span')
# numlist = []
# for tag in tags:
# # Look at the parts of a tag
#     numlist.append(int(tag.contents[0]))
# total = sum(numlist)
# print numlist
# print total

# ex19: Repeatly find the herf and go to another link (assignment for beautifulsoup)
# import urllib
# from BeautifulSoup import BeautifulSoup
# url = raw_input('Enter - ')
# if len(url) == 0:
#     url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
# counts = raw_input('Enter count:')
# if len(counts) == 0:
#     counts = 4
# position = raw_input('Enter position:')
# if len(position) == 0:
#     position = 3
# for count in range(int(counts)+1):
#     print position
#     print 'Retrieving:', url
#     html = urllib.urlopen(url).read()
#     soup = BeautifulSoup(html)
#     tags = soup('a')
#     temp = []
#     for tag in tags:
#         y = tag.get('href')
#         temp.append(y)
#     result = temp[int(position)-1]
#     print 'The third name:', result, '\n'
#     url = result

# ex20: sum up the xml file on the web
# import urllib
# import xml.etree.ElementTree as ET
# url = 'http://python-data.dr-chuck.net/comments_305832.xml'
# data = urllib.urlopen(url).read()
# tree = ET.fromstring(data)
# counts = tree.findall('.//count')
# total = []
# for count in counts:
#     total.append(int(count.text))
# print sum(total)

# ex21: test of Xpath
# import xml.etree.ElementTree as ET
# data = '''
# <bookstore>
# 
# <book>
#     <title lang="eng">Harry Potter</title>
#     <price>29.99</price>
# </book>
# 
# <book>
#     <title lang="eng">Learning XML</title>
#     <price>39.95</price>
# </book>
# 
# </bookstore>'''
# 
# tree = ET.fromstring(data)
# results = tree.findall('book')
# for result in results:
#     print result.find('title').text

# ex22: sum the Json on the web
# import urllib
# import json
# url = 'http://python-data.dr-chuck.net/comments_305836.json' 
# data = urllib.urlopen(url).read()
# info = json.loads(data)
# print json.dumps(info, indent=4)
# count = []
# items = info['comments']
# print items
# for item in items:
#     count.append(int(item['count']))
# print count
# print 'sum: ', sum(count)

# ex23: API assignment use Google location API
# import urllib
# import json
# serviceurl = 'http://python-data.dr-chuck.net/geojson?'
# while True:
#     address = raw_input('Enter location: ')
#     if len(address) < 1:
#         break
#     url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
#     print 'Retrieving', url
#     data = urllib.urlopen(url).read()
#     print 'Retrieved', len(data), 'characters'
#     
#     try: js = json.loads(data)
#     except: js = None
#     if 'status' not in js or js['status'] != 'OK':
#         print '==== Failure To Retrieve ===='
#         print data
#         continue
#     print json.dumps(js,indent=4)
#     result = js['results'][0]['place_id']
#     print result

# ex24: test of sample code sql
# import sqlite3
# 
# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()
# 
# cur.execute('''
#             DROP TABLE IF EXISTS Counts''')
# 
# cur.execute('''
#             CREATE TABLE Counts (email TEXT, count INTEGER)''')
# 
# fname = raw_input('Enter file name: ')
# if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: ') : continue
#     pieces = line.split()
#     email = pieces[1]
#     print email
#     cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (email, count) 
#                     VALUES ( ?, 1 )''', ( email, ) )
#     else : 
#         cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', 
#                     (email, ))
#         # This statement commits outstanding changes to disk each 
#         # time through the loop - the program can be made faster 
#         # by moving the commit so it runs only after the loop completes
#     conn.commit()
# 
#                                                                                                                            # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
# print
# print "Counts:"
# for row in cur.execute(sqlstr) :
#     print str(row[0]), row[1]
# 
# cur.close()

# ex25: assignment count the org and database
# import sqlite3
# conn = sqlite3.connect('database/orgcount.sqlite')
# cur = conn.cursor()
# cur.execute('''
#             DROP TABLE IF EXISTS Counts''')
# cur.execute('''
#             CREATE TABLE Counts (Org TEXT, Count INTEGER)''')
# import urllib
# fname = raw_input('Enter File Name: ')
# if len(fname) < 1:
#     fname = 'mbox.txt'
# fp = open(fname)
# import re
# for line in fp:
#     print 'line: ', line
#     result = re.findall('From:\s\S+@(\S+)', line)
#     if result != []:
#         print result
#         cur.execute('SELECT Count FROM Counts WHERE Org = ?', (result[0], ))
#         row = cur.fetchone()
#         if row is None:
#             cur.execute('INSERT INTO Counts (Org, Count) VALUES (?, 1)', (result[0], ))
#         else:
#             cur.execute('UPDATE Counts SET Count = Count + 1 WHERE Org = ?', (result[0], ))
# sqlstr = 'SELECT Org, Count FROM Counts ORDER BY Count DESC'
# cur.execute(sqlstr)
# r = cur.fetchall()
# for row in r:
#     print row[0], row[1]
# conn.commit()
# cur.close()

# ex26: parsing xml file into db (assignment)
# import xml.etree.ElementTree as ET
# import sqlite3
# 
# conn = sqlite3.connect('database/tracks.sqlite')
# cur = conn.cursor()
# cur.executescript('''
#                  DROP TABLE IF EXISTS Artist;
#                  DROP TABLE IF EXISTS Genre;
#                  DROP TABLE IF EXISTS Album;
#                  DROP TABLE IF EXISTS Track;
#                  
#                   CREATE TABLE Artist (
#                     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                     name TEXT UNIQUE
#                 );
#                 
#                   CREATE TABLE Genre (
#                     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                     name TEXT UNIQUE
#                 );
#                   
#                   CREATE TABLE Album (
#                     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                     artist_id INTEGER,  
#                     title TEXT UNIQUE
#                 );
#                 
#                   CREATE TABLE Track (
#                     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#                     title TEXT UNIQUE,
#                     album_id INTEGER,
#                     genre_id INTEGER,
#                     len INTEGER,
#                     rating INTEGER,
#                     count INTEGER
#                 );''')
# 
# def lookup(d, key):
#     found = False
#     for child in d:
#         if found == True:
#             return child.text
#         if child.tag == 'key' and child.text == key: 
#             found = True
#     return None
# 
# data = open('tracks/Library.xml')
# tree = ET.parse(data)
# dct = tree.findall('dict/dict/dict')
# print 'Dct count: ', len(dct)
# for entry in dct:
#     name = lookup(entry, 'Name')
#     artist = lookup(entry, 'Artist')
#     album = lookup(entry, 'Album')
#     genre = lookup(entry, 'Genre')
#     count = lookup(entry, 'Play Count')
#     rating = lookup(entry, 'Rating')
#     length = lookup(entry, 'Total Time')
#     if name is None or artist is None or album is None or genre is None: continue
#     print 'Name: ', name, 'artist: ', artist, 'album: ', album, 'count: ', count, 'rating; ', rating, 'length: ', length
# # begin to insert into sqlite
#     cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist, ) )
#     cur.execute('''SELECT id FROM Artist WHERE name = ?''', (artist, ))
#     artist_id = cur.fetchone()[0]
# 
#     cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre, ) )
#     cur.execute('''SELECT id FROM Genre WHERE name = ?''', (genre, ))
#     genre_id = cur.fetchone()[0]
# 
#     cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
#                 VALUES (?, ?)''', (album, artist_id))
#     cur.execute('''SELECT id FROM Album WHERE title = ?''', (album, ))
#     album_id = cur.fetchone()[0]
# 
#     cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
#                 VALUES (?, ?, ?, ?, ?, ?)''', (name, album_id, genre_id, length, rating, count))
# 
# print 'SO FAR SO GOOD'
# test = cur.execute('''
#                 SELECT Track.title, Artist.name, Album.title, Genre.name 
#                     FROM Track JOIN Genre JOIN Album JOIN Artist 
#                     ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
#                         AND Album.artist_id = Artist.id
#                     ORDER BY Artist.name LIMIT 3''')
# result = test.fetchall()
# for item in result:
#     print item
# conn.commit()
# conn.close()

# ex27: parsing json and put into database
import json
import sqlite3
conn = sqlite3.connect('database/rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
                 DROP TABLE IF EXISTS User;
                 DROP TABLE IF EXISTS Member;
                 DROP TABLE IF EXISTS Course;

                 CREATE TABLE User (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE
                );

                 CREATE TABLE Course (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                title TEXT UNIQUE
                );
                 
                 CREATE TABLE Member (
                 user_id INTEGER,
                 course_id INTEGER,
                 role INTEGER,
                 PRIMARY KEY (user_id, course_id)
                );''')

fname = open('roster_data.json')
str_data = fname.read()
json_data = json.loads(str_data)
for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    #print 'name: ', name, 'title: ', title, 'role: ', role
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id =  cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id =  cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
                VALUES (?, ?, ?)''', (user_id, course_id, role))

conn.commit()
conn.close
