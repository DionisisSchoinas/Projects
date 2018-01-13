import urllib2
import json
import datetime

picks = [""]*10
for i in range(10):
	exit = True
	while exit:
		#x = i+1    !!! for testing only !!!
		x = raw_input("Give number %s : "%(i+1))
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
cur_month = n.month
cur_day = n.day
cur_min = n.minute
if n.hour in range(0,9):
	cur_min = 55
	cur_day = cur_day -1
a = datetime.datetime(n.year, cur_month, 1, 9, 00)
c = datetime.datetime(n.year, cur_month, cur_day , 23, cur_min - cur_min%5)
b = datetime.datetime(n.year, cur_month, cur_day)
daily_wins = []
winning_days = []
exit1 = True
while exit1:		
	i = 0
	exit2 = True
	d = datetime.datetime(n.year, cur_month, b.day, 23, 55)
	now = b.strftime("%d-%m-%Y")
	url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json"%now
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	data = response.read()
	data = json.loads(data)
	while exit2:	
		exit3 = True
		wins = 0 
		got = 0
		while exit3:			
			x = data['draws']['draw'][i]['results']
			for m in range(10):
				if picks[m] in x:
					got+=1
			if got>10:
				wins+=1
			y = data['draws']['draw'][i]['drawTime']
			y = datetime.datetime.strptime(y, '%d-%m-%YT%H:%M:%S')
			i += 1
			if y<a or y>=c or y>=d:
				exit3 = False				
		daily_wins.append(wins)
		if y<a or y>=c or y>=d:
			exit2 = False
	if y<a:
		exit1 = False
	winning_days.append(now)
	b = b - datetime.timedelta(days=1)
print "You could have had most wins in : "+winning_days[daily_wins.index(max(daily_wins))]
