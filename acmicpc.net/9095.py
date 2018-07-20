t = int(input())
n_list = [0]
m1 = 1
m2 = 2
m3 = 4

for i in range(t):	# 입력을 총 t번 받음
	total = 0
	n = int(input())
	if n == 1:
		total = m1
	elif n == 2:
		total = m2
	elif n == 3:
		total = m3
	else:
		while sum(n_list) <= n-3:
			n_list.append(3)
		n_list.append(int(n%3))

		print(n_list)

		for i2 in range(len(n_list)):
			a = n_list.pop()
			if a == 3:
				n_list.append(2)
				n_list.append(1)
				total += 1
			elif a == 2:
				n_list.append(1)
				n_list.append(1)
				total += 1
			elif a == 1:
				total


	print(total)
n_list.clear()
total = 0