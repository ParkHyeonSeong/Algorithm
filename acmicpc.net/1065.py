'''
어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때,
1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
'''

def A1(i):
	flag = 0
	temp = 0	# 임시 저장 변수
	list_1 = list(i)	# 리스트에 자리수만큼 넣고

	if len(list_1) >= 3:	# 3자리 이상일때만 공식을 적용하고
		temp = int(list_1[0]) - int(list_1[1])	# 등차수열 공식을 확인하고
		for i2 in range(1,len(list_1)-1):
			if int(list_1[i2]) - int(list_1[i2+1]) == temp:
				flag = 1
			else:
				flag = 0

		if flag == 1: # 등차수열이 맞으면
			return int(i)
		else:	# 아니면 0 리턴함
			return 0

	else:	# 아니면 고대로 통과
		return int(i)

# 전역파트
list_all = []
for i in range(1,int(input())+1):	# 입력받은만큼 반복
	temp = A1(str(i))		# 리스트에 추가
	if temp == 0:	# 없으면 추가안함
		temp
	else:	# 있으면 추가함
		list_all.append(temp)

print(len(list_all))