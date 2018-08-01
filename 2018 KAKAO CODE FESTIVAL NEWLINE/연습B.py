from itertools import permutations

line = ['A','C','F','J','M','N','R','T']	# 서있는 상태 저장
# A:어피치 C:콘 F:프로도 J:제이지 M:무지 N:네오 R:라이언 T:튜브
commands = []
stack = 0

for i in range(int(input())):	# n(1 ≤ n ≤ 100)
	commands.append(input())	# 조건저장

for cycle in permutations(line):# 조합을 하나씩 모두 비교

	flag = 0	# 오류감지 플래그

	for command in commands:	# 조건저장을 하나씩 비교
		check = list(command)
		if flag == 0:
			if check[3] == "=":			# 자리수가 한정되있는경우
				temp = (cycle.index(check[0]) - cycle.index(check[2]))
				if temp < 0:				# 음수를 양수로 변경해야함
					temp = temp * (-1) - 1	# 그 후에 -1을 해줌으로써 사이의 프렌즈의 수를 검출
				else:
					temp -= 1
				if temp == int(command[4]):	# 비교
					check.clear()
				else:						# 오류
					flag = 1				# 오류감지 플래그 설정
					check.clear()
					break					# 탈출

			elif check[3] == "<":			# 미만일때
				temp = (cycle.index(check[0]) - cycle.index(check[2]))
				if temp < 0:
					temp = temp * (-1) - 1
				else:
					temp -= 1
				if temp < int(command[4]):
					check.clear()
				else:
					flag = 1
					check.clear()
					break

			elif check[3] == ">":			# 초과일때
				temp = (cycle.index(check[0]) - cycle.index(check[2]))
				if temp < 0:
					temp = temp * (-1) - 1
				else:
					temp -= 1
				if temp > int(command[4]):
					check.clear()
				else:
					flag = 1
					check.clear()
					break

	if flag == 0:
		stack += 1

print(stack)