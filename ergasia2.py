import urllib2
import json
import datetime

def Read_Picked():
	while True:
		a = [""]*10
		x = raw_input("Give 10 different numbers in [1,80] and with spaces in between \n")
		y = x.split(" ")
		while True:
			if y[-1]=="":
				y.remove(y[-1])
			else:
				break
		if 	len(y)!=10:
			del a
			continue
		else:
			try:
				for i in range(len(y)):
					a[i] = int(y[i])
					if not(a[i] in range(1,81)):
						print "Numbers in [1,80]"				
						del a		
						break
					else:
						k = 0
						for j in range(len(a)):
							if a[j]==a[i]:
								k+=1
						if k>=2:
							print "Different numbers"
							del a
							break
				if len(a)==10:
					break
				else:
					del a
					continue
			except:
				continue
	return a 
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


picks = Read_Picked()
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