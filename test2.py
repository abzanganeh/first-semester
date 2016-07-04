import re
txt=raw_input('Please enter your file name: ')
try:
	r=open(txt)
except:
	print 'Please enter a valid file name'
	quit()

total=0
lst=list()
for i in r:
	lst=re.findall('[0-9]+',i)+lst
for num in lst:
	total=int(num)+total
print 'Sum of all numbers in your text is: ',total

