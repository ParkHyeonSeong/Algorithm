import datetime

def GetDayName(a,b):
    days = ['MON','TUE','WED','THU','FRI','SAT','SUN']  # 요일 등록
    return days[datetime.date(2007,a,b).weekday()]  # 요일 구하는 함수

a,b = input().split(" ")    # 다중 입력을 위한 스플릿
print(GetDayName(int(a),int(b)))    # 함수에 맞는 자료형 변환