t = int(input())

for i in range(t):
	s = list(input())
	depth = 1
	out = 0

	for i2 in range(len(s)):
		if s[i2] == "O":
			out += depth
			depth += 1	# 연속증가
		elif s[i2] == "X":
			depth = 1	# 연속초기화


	print(out)
	s.clear()