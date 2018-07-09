num = int(input())

for i in range(num,0,-1):
    temp = "*"*i
    print(temp.rjust(num))