t=input()
a=""
for i in range(8):
	a += t.split(" ")[i]
if a == "12345678":
	print("ascending")
elif a == "87654321":
	print("descending")
else:
	print("mixed")

# 다른 방법도 있겠지만 그냥 스페이스바가 없는 걸로 비교하는게 제일 좋을 것 같아서..?