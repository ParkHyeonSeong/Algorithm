n = int(input())
now = input().split(" ")
high = 0
now2 = []
for i in now:
    now2.append(int(i))
avg = sum(now2)/n

for i in range(n):
    if int(now[i]) >= int(high):
        high = int(now[i])

print ("%.2f" % (avg/high*100))