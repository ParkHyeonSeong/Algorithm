string = input()

try :
    lists = list(string.split(" ")) # 공백을 기준으로 스플릿 -> 리스트화
    while lists.count("") != 0 :    # 공백만 있거나 공백이 리스트로 생성되는 경우 삭제함
        lists.remove("")
    print(len(lists))  # 리스트 개수 새기
except:
    print(0)