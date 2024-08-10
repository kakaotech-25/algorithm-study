# 트럭 1대 주차 1분에 A원
# 트럭 2대 주차 1분에 한 대당 B원
# 트럭 3대 주차 1분에 한 대당 C원
# 상근이는 트럭 3대

time=[0]*100
a, b, c = map(int,input().split())

for _ in range(3):
    start, end = map(int,input().split())
    for i in range(start, end):
        time[i] += 1

re=0
for i in time:
    if i == 0:
        re+=0
    elif i == 1:
        re += a

    elif i==2:
        re+=(b*2)

    elif i == 3:
        re+=(c*3)

print(re)
