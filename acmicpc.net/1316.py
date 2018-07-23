'''
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서,
각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고,
kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다.
둘째줄부터 N개의 줄에 단어가 들어온다.
단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
'''

def act(temp):
	t = int(temp)						# str -> int 변환
	s = []								# 리스트 선언
	save = []
	count = 0							# 연속된 단어가 몇 개인지 카운트
	flag = 0							# 플래그

	for i in range(t):						# 입력된 만큼 입력 반복
		s.append(input())

	for i in range(t):							# 입력된 단어하나하나씩 시행
		l = list(s[i])							# 단어를 한 스펠링으로 분할
		l.append("0")							# 끝을 표시하기 위한 알파벳이 아닌 단어

		for i in range(len(l)-1):			# 글자 길이 수-1 만큼 반복
			if flag == 0:					# 연속된 단어가 중간에 끊겼을때
				if l[i] != l[i+1]:				# 단어가 달라졌을때
					if save.count(l[i]) != 0:			# 이미 반복된었다가 끊긴것이 확인되면
						flag = 1					# 플래그를 설정하고
					else:
						save.append(l[i])				# 아직 사용되지않은 알파벳이라면 리스트에 추가


		if flag == 0:	# 연속된 문자였다면
			count += 1	# 카운트 1 늘리고 공식 끝

		flag = 0	# 초기화파트
		l.clear()
		save.clear()

	return count

# 전역 파트
print(act(input()))