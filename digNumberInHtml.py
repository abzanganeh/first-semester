import re
import urllib
from BeautifulSoup import *
url= raw_input('Enter:')

try:
	html=urllib.urlopen(url).read()
except:
	print"Not a valid URL"
	quit()
soup= BeautifulSoup(html)

spn=soup('span')
sum=0
num=[]
count=0
for i in spn:
	i=str(i)
	num=re.findall(">([0-9]+)<",i)+num
for j in num:
	j=int(j)
	sum=j+sum
	count+=1
print count
print sum