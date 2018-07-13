c = int(input())    # 테스트케이스

for i in range(c):
    _input = input().split(" ") # 학생수와 평균을 받음
    n = int(_input[0])   # 학생수를 빼내고
    del _input[0]   # 리스트에서 삭제

    trans_input = []

    for i2 in _input:
        trans_input.append(int(i2))   # 변환 후 재 리스트화

    avg = sum(trans_input)/n    # 평균값 검출

    n_high = 0

    for i3 in trans_input:
        if i3 > avg:   # 점수 비교
            n_high += 1

    print(("%.3f" % (n_high/n*100)) + "%")
