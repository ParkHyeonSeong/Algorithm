import sys
c = sys.stdin.readline().rstrip()
for i in range(0,int(c)):
    a,b = sys.stdin.readline().rstrip().split(" ")
    sys.stdout.write(str(int(a)+int(b))+"\n")

# 뻘짓하다가 메모리초과만 10번가까이 냈다
# 이유는 입력을 받고 저장하지않고 바로 더한 값을 출력하면 빠르게 진행된다
# 문제를 다른 방식으로 접근하는 눈을 가져야겠다.