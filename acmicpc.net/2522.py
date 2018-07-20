n = int(input())

f = 1
b = n

while f != n :
	temp = "*"*f
	print(temp.rjust(n))
	f += 1	# 표시되는 별의 갯수 증가

while b != 0 :
	temp = "*"*b
	print(temp.rjust(n))
	b -= 1	# 표시되는 별의 갯수 증가