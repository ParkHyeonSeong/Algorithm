n = int(input())
_min = [n]
_min.append(0)  # 조건 명시
_min.append(1)  # 조건 명시
_min.append(1)  # 조건 명시

temp = 0    # 비교를 위한 임시 저장

for i in range(4,n+1):
    _min.append(_min[i-1] + 1) # 최대횟수 설정

    if i % 2 == 0:  # 나눠질때
        temp = _min[i // 2] + 1  # 자신이 나뉘어진 숫자의 최소횟수보다
        if temp < _min[i]:  # 적으면
            _min[i] = temp  # 그것이 즉 최소 횟수

    if i % 3 == 0:
        temp = _min[i // 3] + 1
        if temp < _min[i]:
            _min[i] = temp

print(_min[n])