
import sys

personName = sys.argv[1]

print "Hello " + personName
TimeTable = int(sys.argv[2])
NumSteps = int(sys.argv[3])
for i in range (1,NumSteps):
	print str(TimeTable) + " x " + str(i) + " = " str(TimeTable*i)
	