# 아 공식을 세우면 쉽게 풀리는 문제인데 자그마치 3시간정도 걸렸다...
# 아직 동적프로그래밍의 개념이 잡히지 않은듯 하다...

t = int(input())

for i in range(t):	# 입력을 총 t번 받음	
	n_list = [0,1,2,4]
	flag = 1
	n = int(input())
	if n == 1:
		total = n_list[1]
		flag = 0
	elif n == 2:
		total = n_list[2]
		flag = 0
	elif n == 3:
		total = n_list[3]
		flag = 0

	if flag == 1:
		for i in range(4,n+1):
			n_list.append(n_list[i-1] + n_list[i-2] + n_list[i-3])
		print(str(n_list[len(n_list)-1]))
	else :
		print(total)
		flag = 1

	n_list.clear()