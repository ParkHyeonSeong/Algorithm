t = int(input())	# 테스트 케이스

for i in range(t):
	l = []
	s = input()
	r = int(s.split(" ")[0])	# 몇번 반복할지 변수 저장
	l = list(s.split(" ")[1])	# 문자열을 리스트화 시켜서 하나씩 저장
	for i2 in l:
		print(i2*r,end = "")	# r번 반복해서프린트
	print("")