import urllib2
import json
import datetime

def Read_Picks(picks):
	for i in range(10):
		exit = True
		while exit:
			#x = i+1    #!!! for testing only !!!
			x = raw_input("Give number %s : "%(i+1))
			try:
				x = int(x)
				if x in range(1,81) and not(x in picks):
					exit = False
					picks[i] = x
				else:
					print "Give a number between 1-80 and pick each number ones"
			except:
				print "Give a number between 1-80"
def Fix_Time(n):
	cur_day = n.day
	if n.hour in range(0,9):
		cur_day = cur_day -1
	return cur_day
def Find_Wins(data,i):
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
	return wins
def Pull_Data(b):
	now = b.strftime("%d-%m-%Y")
	url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json"%now
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	data = response.read()
	data = json.loads(data)
	return data
def Save_Wins(b):
	data = Pull_Data(b)
	i = 0
	wins = Find_Wins(data,i)
	daily_wins.append(wins)
	winning_days.append(b.strftime("%d-%m-%Y"))


picks = [""]*10
Read_Picks(picks)
n = datetime.datetime.now()
day = Fix_Time(n)
a = datetime.datetime(n.year, n.month, 1)
b = datetime.datetime(n.year, n.month, day)
daily_wins = []
winning_days = []
while b>=a:
	Save_Wins(b)
	b = b - datetime.timedelta(days=1)
the_day = daily_wins.index(max(daily_wins))
if max(daily_wins) == 0:
	print "Woah you are unlucky , no wins ever"
	print  "How ?"
else:
	print "You could have had most wins in : "+winning_days[the_day]