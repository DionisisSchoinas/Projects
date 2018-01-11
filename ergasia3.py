
text = open("my_text.txt","r")
chars = []
k=0
for li in text:
	for c in li:
		k=k+1
		chars.append(c)
print k
print chars
asci = range(ord('A'),ord('Z')+1)+range(ord('a'),ord('z')+1)
for i in range(k):
	x = ord(chars[i])
	if x in asci:
		leto = asci.index(x)
		if leto<39:
			letn = leto+13			
		else:
			letn = -(51-leto)+13
		value = asci[letn]
		chars[i] = chr(value)
		print chars
text.close()