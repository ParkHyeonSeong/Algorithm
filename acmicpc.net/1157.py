'''
문제
알파벳 대소문자로 된 단어가 주어지면,
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

def action(string):
	s = list(string)	# 리스트화 시켜서 1개씩 나눠 저장
	cp = []
	count = 0
	result = "?"

	for i in range(65,91):
		if count == s.count(chr(i))+s.count(chr(i+32)):	# 중복되는 경우
			cp.clear()					# 리스트를 초기화 시키고 카운트는 변화시킬 필요가 없음
			count = s.count(chr(i))+s.count(chr(i+32))
		elif count < s.count(chr(i))+s.count(chr(i+32)):		# top횟수가되는경우
			cp.clear()
			cp.append(chr(i))								# 대문자로 리스트에 저장하고
			count = s.count(chr(i))+s.count(chr(i+32))		# 몇 번 나왔느니 저장

	if len(cp) == 0:					# 리스트가 비어있는 경우
		return "?"
	else :
		return cp[0]					# 아니라면 리스트 리턴

print(action(input()))