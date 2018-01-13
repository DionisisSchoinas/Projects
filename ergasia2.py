import urllib2
import json
import datetime

picks = [""]*10
for i in range(10):
	exit = True
	while exit:
		x = i+1
		#x = raw_input("Give number %s : "%(i+1))
		try:
			x = int(x)
			if x in range(1,81) and not(x in picks):
				exit = False
				picks[i] = x
			else:
				print "Give a number between 1-80 and select each number ones"
		except:
			print "Give a number between 1-80"
n = datetime.datetime.now()
a = datetime.datetime(n.year, n.month, 1, 9, 00)
c = datetime.datetime(n.year, n.month, n.day , 23, n.minute-n.minute%5)
b = datetime.datetime(n.year, n.month, n.day)	
f = []
exit1 = True
while exit1:		
	i = 0
	exit2 = True
	d = datetime.datetime(n.year, n.month, b.day, 23, 55)
	now = b.strftime("%d-%m-%Y")
	url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json"%now
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	data = response.read()
	data = json.loads(data)
	while exit2:	
		exit3 = True
		while exit3:			
			x = data['draws']['draw'][i]['results']
			#f.append(x)
			y = data['draws']['draw'][i]['drawTime']
			y = datetime.datetime.strptime(y, '%d-%m-%YT%H:%M:%S')
			print i , y
			i += 1
			if y<a or y>=c or y>=d:
				print "3"
				exit3 = False	
		if y<a or y>=c or y>=d:
			print "2"
			exit2 = False
	if y<a:
		print "1"
		exit1 = False
	b = b - datetime.timedelta(days=1)