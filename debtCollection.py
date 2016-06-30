import sys
import MySQLdb
analysis=sys.argv[1]
#this is the line to connect to our MYSQL
db=MySQLdb.connect(host="localhost",user="root",passwd="gdia5bm",db="sales")

#you must create a cursor object
#it will let you execute all the queries you need

cur=db.cursor()
#command = "SELECT * FROM transactions WHERE status='" + analysis +"'"
command = "SELECT * FROM transactions as t join info i on t.name = i.name WHERE status='" + analysis +"'"

print command
#cur.execute("SELECT * FROM transactions WHERE status='pending'")
cur.execute(command)

for row in cur.fetchall():
	print row[2],row[9]

db.close