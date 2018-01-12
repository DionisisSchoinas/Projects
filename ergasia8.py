import random
import time

start_time = time.time()
num = random.sample(range(-29,30),30)
comb = []
f = 0
print num
for i in range(30):
	x = num[i]
	for j in range(i+1,30):
		y = num[j]
		for k in range(j+1,30):
			if -x == y+num[k] :
				f = f+1
				comb.append([x,y,num[k]])
if comb == []:
	print "Den uparxoun triades"
else:
	for i in range(f):
		print comb[i]
print time.time() - start_time