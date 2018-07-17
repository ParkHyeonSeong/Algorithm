x = int(input())  # 최종값을 입력 받음

have = [0,64] # 가지고 있는 막대를 리스트에 추가함(0은 논리적으로 쉬우라고..)
total = 64  # 막대기 길이의 총합
temp = 0    # 임시 저장
count = 1   # 카운트


while total > x:  # 막대의 합이 최종값보다 같거나 클때까지 반복
    temp = have.pop()       # 마지막 값을 팝!
    have.append(temp//2)    # 막대기를 절반하여 넣음
    have.append(temp//2)    # 막대기를 절반하여 넣음 2
    count += 1              # 결과적으로 막대기 수가 1개 늘음

    if sum(have) - have[count] >= x:    # 자른 것중 1개를 버리고 남은 막대의 길이가 x보다 크거나 같다면
        del have[count] # 막대기하나를 버림
        count -= 1

    total = sum(have)       # 살아남은 막대기를 모두 붙임

print(count)