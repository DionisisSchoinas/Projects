in_text=raw_input("Give the file you want to encode (.txt)\n")
try:
	text = open(in_text,"r")
	chars = []
	k=0
	for li in text:
		for c in li:
			k=k+1
			chars.append(c)
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
	output = ""
	output = output.join([str(chars[i]) for i in range(k)])
	out_text=raw_input("Give the name of the file you want to save the encoded message (.txt)\n")
	enc = open(out_text,"w")
	enc.write(output)
	text.close()
	enc.close()
except:
	print "File not found"