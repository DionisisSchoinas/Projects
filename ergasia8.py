import random
import time

def findCombos(comb):
	f = 0
	num = random.sample(range(-29,30),30)
	for i in range(30):
		x = num[i]
		for j in range(i+1,30):
			y = num[j]
			for k in range(j+1,30):
				if -x == y+num[k] :
					f = f+1
					comb.append([x,y,num[k]])
	return f
def Print(comb,f):
	if comb == []:
		print "Den uparxoun triades"
	else:
		print "bhka"
		print f
		for i in range(f):
			print comb[i]
			
start_time = time.time()
comb = []
f = findCombos(comb)
Print(comb,f)
print time.time() - start_time