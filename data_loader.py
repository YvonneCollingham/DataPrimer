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
print "\n\n"
for line in f:
	if line.startswith('date'):
		pass
	else:
		line=line.strip('\n').strip('\r')
		entry=line.split(',')

		print " "
		print entry
		#print "INSERT INTO transactions(date,name,cost,paid,balance,status) VALUES('"+entry[1]+","+entry[2]+","+entry[3]+","+entry[4]+","+entry[5]+"')"
		#print "INSERT INTO transactions(date,name,cost,paid,balance,status) VALUES('"+entry[0]+"','"+entry[1]+"','"+entry[2]+"','"+entry[3]+"','"+entry[4]+"','"+entry[5]+"')"
		
		query = "INSERT INTO transactions(date,name,cost,paid,balance,status) VALUES('"+entry[0]+"','"+entry[1]+"','"+entry[2]+"','"+entry[3]+"','"+entry[4]+"','"+entry[5]+"');"
		print " "
		print query
		print "--------------------------------------"
		cur.execute(query)
		db.commit()
		#try:
		#	cur.execute(query)
		#except:
		#	pass