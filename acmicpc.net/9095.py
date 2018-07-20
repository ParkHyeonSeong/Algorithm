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
		while sum(n_list) + 3 <= n:
			n_list.append(3)
		while sum(n_list) + 2 <= n:
			n_list.append(3)
		while sum(n_list) + 1 <= n:
			n_list.append(3)

		for i2 in range(len(n_list)):
			print(n_list)
			print(total)
			a = n_list.pop()
			if a == 3:
				n_list.append(2)
				n_list.append(1)
				total += 1
			elif a == 2:
				n_list.append(1)
				n_list.append(1)
				total += 1
			elif a == 1 and n_list.count(1) != n+1:
				n_list.insert(1,1)
				total += 1



	print(total)
n_list.clear()
total = 0