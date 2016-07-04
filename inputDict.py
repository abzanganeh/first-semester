import string
fname = raw_input("Enter file name: ")

try:
	a = open(fname)
except:
	print "Invalid path or file name"
lst=[]
d={}
for line in a:
    
    lst=line.split()+lst
lst=lst.translate(None, string.punctuation)
for i in lst:
	d[i]=d.get(i,0)+1
   
print d
