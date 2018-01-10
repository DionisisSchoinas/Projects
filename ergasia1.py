from __future__ import division
import random
import time

start_time = time.time()
def getNumbers(a):
	numbers=[]
	for i in range(100):
		numbers.append(random.sample(a,5))	
	return numbers
def callNumbers(choice,a):
	k=[0]*80
	exit=True
	bingo=0
	while exit:
		bingo=bingo+1
		x=random.sample(a,1)
		a.remove(x[0])
		for i in range(0,80):
			if x[0] in choice[i]:
				k[i]=k[i]+1
				if k[i]==5:
					exit=False
	return bingo

bingos=0
for i in range(1000):
	a=range(1,81)
	players=getNumbers(a)
	bingos=bingos+callNumbers(players,a)
print bingos/1000
print time.time() - start_time