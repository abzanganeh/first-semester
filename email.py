# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
	fh = open(fname)
except:
	print "Invalid path or file name"
count = 0
for line in fh:
    if not line.startswith("From ") : continue
    temp=[]
    temp=line.split()
    print temp[1]
    count+=1

print "There were", count, "lines in the file with From as the first word"

