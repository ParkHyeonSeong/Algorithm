total = 1
for i in range(3):
	total = total * int(input())	# 번 반복하여 바로 곱함(저장 효율성 극대화)

t_list = list(str(total))	# 각 자리를 리스트화시켜서
for i in range(10):	# 길이만큼 반복
	print(t_list.count(str(i)))	