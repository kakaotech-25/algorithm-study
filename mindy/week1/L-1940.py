# 투포인터 문제
# 투포인터 문제의 경우 보통 정렬해서 풀이

import sys

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

k = list(map(int,input().strip().split()))
cnt =0 
k.sort()

left, right = 0,len(k)-1

while left<right:
    sum = k[left]+k[right]
    if sum < m:
        left +=1
    elif sum > m:
        right -=1
    else:
        cnt+=1
        left+=1
        right -=1
 
print(cnt)               
        