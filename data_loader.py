import sys
import MySQLdb

#this is the line to connect to our MYSQL
db=MySQLdb.connect(host="localhost",user="root",passwd="gdia5bm",db="sales")

#you must create a cursor object
#it will let you execute all the queries you need

cur=db.cursor()

cur.execute("SELECT * FROM info")
for row in cur.fetchall():
	print row

f=open("primer.csv","r")

for line in f:
	line=line.strip('\n').strip('\r')
	entry=line.split(',')
	print entry