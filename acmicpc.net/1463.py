n = int(input())
count = 0

while(n != 1):
    if n%3 == 0:  # 3으로 쪼개질때
        n /= 3
        count += 1
    elif n % 2 == 0:  # 2로 쪼개지면 2분의1로 잘라질 수 있음
        if (n-1) % 3 == 0:  # 그러나 1을 빼고 3분의1로 자르면 더 작아질 수 있으므로
            n -= 1
            n /= 3
            count += 2
        else:
            n /= 2
            count += 1
    else:   # 2와3의 배수 모두 해당하지않으면 1을 뺌
        n -= 1
        count += 1

print(count)