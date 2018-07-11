string_ = input()  # 총 문장 받기
trans_list = list(string_) # 문장이 몇글자인지 새기 위해 리스트로 만듦
show_list = []  # 단위로 끊어서 저장하기 위한 리스트
count = 0   # 10글자로 쪼개지지 못한 글자를 확인하기위해 10단위로 카운트 증가

try:
    for i in range(0,len(trans_list),10):
        show_list.append(string_[i] + string_[i+1] + string_[i+2] + string_[i+3] + string_[i+4] + string_[i+5] + string_[i+6] + string_[i+7] + string_[i+8] + string_[i+9])  # 처음부터 끝가지 int형으로 변환하면서 리스트화
        count += 1  # 10개추가되었음을 확인
except :
    if len(trans_list)%10 != 0: # 10개 후 남는 것이 있는지 확인
        temp = []
        for i in range(count*10, len(trans_list)):  # 10단위 후부터 남은 길이까지 반복
            temp.append(string_[i])

        show_list.append("".join(temp))   # 1글자씩 분리된거 합치고 리스트추가
    count +=1   # 줄 수 추가

for i in range(0,count):
    print(show_list[i])  # 줄 수 띄면서 10개씩 끊은 요소 출력