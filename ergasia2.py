import urllib2
import json
import datetime

picks = [""]*10
for i in range(10):
	exit = True
	while exit:
		x = i+1    #!!! for testing only !!!
		#x = raw_input("Give number %s : "%(i+1))
		try:
			x = int(x)
			if x in range(1,81) and not(x in picks):
				exit = False
				picks[i] = x
			else:
				print "Give each number ones"
		except:
			print "Give a number between 1-80"
n = datetime.datetime.now()
cur_month = n.month
cur_day = n.day
cur_min = n.minute
if n.hour in range(0,9):
	cur_min = 55
	cur_day = cur_day -1
a = datetime.datetime(n.year, cur_month, 1)
b = datetime.datetime(n.year, cur_month, cur_day)
daily_wins = []
winning_days = []
while b>=a:
	now = b.strftime("%d-%m-%Y")
	url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json"%now
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	data = response.read()
	data = json.loads(data)
	i = 0
	wins = 0 
	for j in data['draws']['draw']:	
		got = 0	
		x = data['draws']['draw'][i]['results']
		for m in range(10):
			if picks[m] in x:
				got+=1
		if got>4:
			wins+=1
		i+=1
	daily_wins.append(wins)
	winning_days.append(now)
	b = b - datetime.timedelta(days=1)
the_day = daily_wins.index(max(daily_wins))
print daily_wins
print winning_days
print the_day
if max(daily_wins) == 0:
	print "Woah you are unlucky , no wins ever"
	print  "How ?"
else:
	print "You could have had most wins in : "+winning_days[the_day]