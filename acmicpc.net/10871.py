import sys

n,x = input().split()
row = input().split()
lists = []

for i in row:
    if int(i) < int(x):
        lists.append(i)

for i in lists:
    sys.stdout.write(i + " ")