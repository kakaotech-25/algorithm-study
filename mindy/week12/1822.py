# 이분탐색으로 풀려고 했는데 오히려 시간초과...
# 차집합
import sys

input = sys.stdin.readline

a, b = map(int, input().split())

arr = set(map(int,input().split()))

brr = set(map(int,input().split()))
k =sorted(arr.difference(brr))
print(len(k))
print(' '.join(map(str,k)))
"""arr.sort()
cnt=0

re = arr.copy()
re = list(re)

for i in brr:
    left, right = 0, a-1
    while left <= right:
        mid = (left+right)//2
        #print(mid)
        if arr[mid] == i:
            cnt +=1
            re.remove(i)
            break
        elif arr[mid] >i:
            right = mid-1
        else:
            left = mid+1

print(len(arr)-cnt)
if (len(arr)-cnt):
    print(' '.join(map(str,re)))
    
"""