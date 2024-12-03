import sys

input = sys.stdin.readline

n, a, b = map(int,input().split())

# 2개의 차를 구하고 그 차를 기준으로 정렬? 한다음 a개 b개로 나누기

arr =[]
lst =[]

for i in range(n):
    x, y =map(int,input().split())
    arr.append([x,y])
    lst.append([x-y,i])

lst.sort(key=lambda x: x[0])

re =0

for i in range(n):
    id = lst[i][1]
    if a!=0:
        a-=1
        re+=arr[id][0]
    else:
        re+=arr[id][1]
print(re)