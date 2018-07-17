n = int(input())    # 배열 제한
a = []
b = []
_list = input()
for i in range(n):
    a.append(int(_list.split(" ")[i]))  # str - > int
_list = input()
for i in range(n):
    b.append(int(_list.split(" ")[i]))  # str - > int

a.sort()                # 오름차
b.sort(reverse=True)    # 내림차

total = 0
for i in range(n):
    total += a[i] * b[i]

print(total)