num = str(input())  # 입력 받기
temp = []   # 리스트 초기화

temp.extend(list(num)) # 리스트에 스플릿
if len(temp) == 1:  # 주어진 수가 10보다 작다면 0을 붙여 두 자리수를 만듦
    temp.clear()
    temp.append("0")
    temp.extend(list(num))  # 재스플릿
    num = "0" + num

t1 = int(temp[0])   # 변수 할당
t2 = int(temp[1])
temp.clear()    # 할당 후 재사용을 위해 초기화

f_num = "0" # 비교를 위한 임시저장 변수
count = 0

while num != f_num: # 입력값과 계산된 값이 같을 떄까지 반복
    temp.extend(list(str(t1+t2)))   # 앞자리와 뒷자리를 더해서 다시 스플릿

    if len(temp) == 1:  # 결과값이 10보다 작다면 0을 붙여 두 자리수를 만듦
        temp.clear()
        temp.append("0")
        temp.extend(list(str(t1+t2)))  # 재스플릿

    f_num = str(t2) + str(temp[1])  # 결과값과 더해진 숫자의 일의 자리를 str로 합하여 저장 # 이 문장 들여쓰기 잘못해서 시간초과됐었다..;

    t1 = t2
    t2 = int(temp[1])    # 결과값의 뒷자리를 t2로 할당
    temp.clear()  # 할당 후 재사용을 위해 초기화

    count += 1  # 싸이클 + 1


print(count)