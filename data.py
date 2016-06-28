import sys
Status = sys.argv[1]
f=open("primer.csv","r")
#print f
TotalBalance = 0
TotalCost = 0
TotalPaid = 0
for line in f:
	try:
		#line = line.strip('\n').strip('\r')
		line = line.strip('\n')
		entry = line.split(',')
		TotalBalance += int(entry[4])
		TotalCost += int(entry[2])
		TotalPaid += int(entry[3])
	except:
		print "bad line ", line
		#pass
print "\nBalance total = ", TotalBalance
print "Cost total = ", TotalCost
print "Paid total", TotalPaid


#f.close
#f=open("primer.csv","r")
f.seek(0)
print "\nStatus " + Status
count = 0
TotalBalance = 0
TotalCost = 0
TotalPaid = 0
for line in f:
	try:
		line = line.strip('\n')
		entry = line.split(',')
		if entry[5]==Status:
			print entry[1]
			count +=1
			TotalBalance += int(entry[4])
			TotalCost += int(entry[2])
			TotalPaid += int(entry[3])
	except:
		pass
print "\nCases that are " + Status + " = " + str(count)
print Status + " Balance total = ", TotalBalance
print Status + " Cost total = ", TotalCost
print Status + " Paid total", TotalPaid
