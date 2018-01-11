
text = open("my_text.txt","r")
chars = []
for li in text:
	for c in li:
		chars.append(c)
print chars