from __future__ import division
import random

def getNumbers(numbers):
	for i in range(0,100):
		numbers.append([])
		for j in range(5):
			while True:
				x = random.randint(1,80)
				if not(x in numbers[i]):
					numbers[i].append(x)		
					break
def callNumbers(choice):
	a=[]
	k=[]
	exit=True
	bingo=0
	for i in range(1,81):
		a.append(i)
		k.append(0)
	while exit:
		bingo=bingo+1
		x=random.sample(a,1)
		a.remove(x[0])
		for i in range(0,80):
			if (x[0] in choice[i]):
				k[i]=k[i]+1
				if k[i]==5:
					exit=False
	return bingo

bingos=0
for i in range(1000):
	players=[]
	getNumbers(players)
	pulled=callNumbers(players)
	bingos=bingos+pulled
print bingos/1000