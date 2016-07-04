
import re
hh=[]
mm=[]
while True:
	
	y=raw_input('Enter working hours:')
	if y=='':
		break
	hh=re.findall('^([0-9]+)\s', y)+hh
	print hh
	mm=re.findall('^[0-9]+\s([0-9]+)',y)+mm
	print mm
hrs=0
min=0
for i in hh:
	hrs=float(i)+hrs
for j in mm:
	hrs=(float(j)/60)+hrs
print hrs 
min=(hrs%int(hrs))*60
hrs=int(hrs)
print 'your worked',hrs,'hours and ',min, 'mins in last month'

