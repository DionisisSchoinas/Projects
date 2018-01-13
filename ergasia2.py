import urllib2
import json
import datetime

cur_date =datetime.datetime.now()
month = cur_date.strftime("%m-%Y")
now = cur_date.strftime("%d-%m-%Y")
url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json"%now
req = urllib2.Request(url)
response = urllib2.urlopen(req)
data = response.read()
data = json.loads(data)
f = []
exit = True
i = 0
while exit:
	times = datadata['draws']['draw'][i]['drawTime']
	x = data['draws']['draw'][i]['results']
	y = list(x)
	f.append(x)
	i+=1
	if not(y[0]=='1' and y[1]=='2'):
		print "in"
		exit = False
for x in range(i):
	print f[x]
