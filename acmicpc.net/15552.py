import sys

c = sys.stdin.readline().rstrip()
t = []

for i in range(0,int(c)):
    a,b = int(sys.stdin.readline().rstrip().split(" "))
    t.append(a+b)

for i in range(0,len(t)):
    print(t[i])