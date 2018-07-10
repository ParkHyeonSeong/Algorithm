length = int(input())   # 숫자개수받음

before_split = input()  # 숫자이어받기
after_split = list(before_split)   # 숫자 리스트화, but str -> int 변환 필요
trans_list = [] # int변환 후 리스트

for i in range(0,length):
    trans_list.append(int(after_split[i]))  # 처음부터 끝가지 int형으로 변환하면서 리스트화

print(sum(trans_list))  # sum을 이용한 리스트 총합