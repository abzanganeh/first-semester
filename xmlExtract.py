import urllib
import xml.etree.ElementTree as ET

url= raw_input('Enter:')
try:
	xml=urllib.urlopen(url).read()
except:
	print"Not a valid URL"
	quit()
counts=[]
print "Retrieving "+ url
print "Retrieved " ,len(xml)," characters."
stuff=ET.fromstring(xml)
for elem in stuff.iter(tag="count"):
	counts.append(int(elem.text))
sum=0
for i in counts:
	sum=sum+i
print "Count: ", len(counts)
print "Sum: ",sum



 print 'Retrieving', url

 print json.dumps(js, indent=4)
  lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
    
    
    
    
​
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'​
​
while True:​
    address = raw_input('Enter location: ')​
    if len(address) &lt; 1 : break​
​
    url = serviceurl + urllib.urlencode({'sensor':'false', ​
          'address': address})​
    print 'Retrieving', url​
    uh = urllib.urlopen(url)​
    data = uh.read()​
    print 'Retrieved',len(data),'characters'​
​
    try: js = json.loads(str(data))​
    except: js = None​
    if 'status' not in js or js['status'] != 'OK':​
        print '==== Failure To Retrieve ===='​
        print data​
        continue​
​
    print json.dumps(js, indent=4)​
​
    lat = js["results"][0]["geometry"]["location"]["lat"]​
    lng = js["results"][0]["geometry"]["location"]["lng"]​
    print 'lat',lat,'lng',lng​
    location = js['results'][0]['formatted_address']​
    print location