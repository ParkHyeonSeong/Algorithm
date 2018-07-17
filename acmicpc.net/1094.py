_in = int(input())  # 최종값을 입력 받음

have = [64] # 가지고 있는 막대를 리스트에 추가함
total = 64  # 막대기 길이의 총합

temp = 0    # 임시 저장
count = 1   # 카운트

while total >= _in:  # 막대의 합이 최종값보다 같거나 클때까지 반복
    temp = have.pop()   # 마지막 값을 팝!
    print(temp)
    have.append(temp/2) # 막대기를 두동강 낸 후 하나를 저장하고
    have.append(temp/2/2) # 절반 중 절반을 하나 버리고 하나를 저장

    total = sum(have)   # 막대기를 모두 붙임
    count += 1  # 카운트++

    print(total)

print(count)