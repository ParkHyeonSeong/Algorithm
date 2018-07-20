t = int(input())
l = []
for i in range(t):
	c = input()	# 명령과 숫자를 받음
	if c.split(" ")[0] == "push":	# 푸시일 경우만 커맨드와 숫자를 나눔
		n = c.split(" ")[1]
		c = c.split(" ")[0]

	if c == "push":	# 푸시면 집어넣고
		l.append(n)
	elif c == "top":	# 탑이면 맨위 출력
		if len(l) == 0:	# 스택이 비어있으면 0
			print("-1")
		else:
			print(l[len(l)-1])
	elif c == "pop":
		if len(l) == 0:	# 스택이 비어있으면 0
			print("-1")
		else:
			print(l.pop())
	elif c == "size":
		print(len(l))
	elif c == "empty":
		if len(l) == 0:	# 스택이 비어있으면 0
			print("1")
		else:
			print("0")