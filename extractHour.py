name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
	handle = open(name)
except:
	print "Invalid path or file name"
hh={}
for line in handle:
	if not line.startswith('From '):continue
	print line
	words=[]
	time=[]
	hour=[]
	words=line.split()
	time=words[5]
	hour=time.split(':')
	hh[hour[0]]=hh.get(hour[0],0)+1
	
lst= hh.items()
lst.sort()
for (a,b) in lst:
	print a,b