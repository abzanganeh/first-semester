fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
	print "Not a valid file name"

lst = list()
for line in fh:
	temp=[]
	line=line.rstrip()
	temp=line.split()
	#print temp
	for i in temp:
		if not i in lst:
			lst.append(i)
#print lst
lst.sort()
print lst



