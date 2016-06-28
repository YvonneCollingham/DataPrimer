import sys

f=open("primer.csv","r")
print f
total = 0
LineNum = 0
for line in f:
	#line = line.strip('\n').strip('\r')
	line = line.strip('\n')
	entry = line.split(',')
	#print entry
	#print entry[4]
	if (LineNum>0):
		total = total + int(entry[4])
	LineNum=LineNum+1
print "Balance total = ", total
f.close