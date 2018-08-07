import math

n, k = input().split()

l = input().split()  # 인형 리스트
l_std = []
std = []

for i in range(int(n)):
    l[i] = int(l[i])  # 인트형으로 변경


for i in range(int(n)-int(k)+1):
    # 초기화
    l_std.clear()

    for i2 in range(int(k)):
        l_std.append(l[i+i2])

    avg = sum(l_std)/len(l_std)

    var = 0
    for i2 in range(len(l_std)):
        var = var + ((l_std[i2]-avg)**2)
    var = var / len(l_std)

    std.append(math.sqrt(var))

temp = std[0]
for i in std:
    if i < temp:
        temp = i

print(temp)
