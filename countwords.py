# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")

try:
	fh = open(fname)
except:
	print "Invalid path or file name"
lst=[]
count = 0
for line in fh:
    fh=fh.rstrip()
    lst=lst+fh.split()
print lst
   


