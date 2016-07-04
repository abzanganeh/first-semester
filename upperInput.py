# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
	print "Invalid path or file name"
	quit()
for i in fh:
	i=i.rstrip()
	print i.upper()
	

	

