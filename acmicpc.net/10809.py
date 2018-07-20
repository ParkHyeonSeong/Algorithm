s = list(input())
out = ""

for i in range(97,123):	# 알파벳 갯수만큼 반복
	try:
		temp = s.index(chr(i))
	except:
		temp = "-1"

	if i != 123:
		out = str(out) + str(temp) + " "
	else:
		out = str(out) + str(temp)
		
print(out)