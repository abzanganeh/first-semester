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



import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location