# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
name=[]
num=[]
tags = soup('a')
for tag in tags:
	num.append(str(tag.get('href',None)))

print num
for i in num:
	i=str(i)
	name=re.findall("_by_([a-z A-Z]+).",i)+name
print name