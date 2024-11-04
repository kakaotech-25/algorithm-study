# 과자 나눠주기
import sys

input = sys.stdin.readline

m, n = map(int,input().split())

arr = list(map(int,input().split()))

left, right =1, max(arr)

re =0
while left<=right:
    log = 0
    mid = (left+right)//2
    for i in arr:
        if i >= mid:
            log += i//mid 
    if log < m:
        right = mid-1
    else:
        re = max(re,mid)
        left  = mid+1
        
    
print(re)