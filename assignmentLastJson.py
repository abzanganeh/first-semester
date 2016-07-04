import urllib
import json
url = raw_input('Enter location: ')
lst=[]
num=0
all=[]
count=0
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
lst=data.split()
for i in lst:
	all=i.split(':')+all
for j in all:
	try:
		if int(j):
			num=int(j)+num
			count+=1
	except:
		continue
print 'Count: ', count
print 'Sum: ', num

			
			
			
	
