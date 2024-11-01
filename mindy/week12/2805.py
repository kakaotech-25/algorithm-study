import sys

input = sys.stdin.readline


n, m  = map(int,input().split())

arr = list(map(int,input().split()))


arr.sort()
left, right =0, max(arr)

re =0
while left<=right:
    log = 0
    mid = (left+right)//2
    for i in arr:
        if i > mid:
            log += i-mid     
    if log < m:
        right = mid-1
    else:
        re = mid
        left  = mid+1
        
    
print(re)