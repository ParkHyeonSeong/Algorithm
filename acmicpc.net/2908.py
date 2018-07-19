t = input()
a = list(t.split(" ")[0])
b = list(t.split(" ")[1])
a2 = int(a[2])*100 + int(a[1])*10 + int(a[0])	# 10진수 구하는 공식처럼 해결
b2 = int(b[2])*100 + int(b[1])*10 + int(b[0])
if a2 > b2 :
	print(a2)
else:
	print(b2)