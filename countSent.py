name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
	handle = open(name)
except:
	print "Invalid path or file name"
email={}
for line in handle:
	if not line.startswith('From '):continue
	words=[]
	words=line.split()
	email[words[1]]=email.get(words[1],0)+1
max=None
for e in email:
	if email[e]>max:	
		key=e
		max=email[e]
	else:
		continue
print key , max		