import urllib
from BeautifulSoup import *
url = raw_input('Enter URL:')
count=raw_input('Enter count:')
position=raw_input('Enter position:')
print 'retrieving:',url
count=int(count)
position=int(position)
i=0
while i<count:
	links=[]
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	for tag in tags:
		links.append(str(tag.get('href',None)))
	url=links[position-1]
	print 'retrieving: ',url
	i+=1
