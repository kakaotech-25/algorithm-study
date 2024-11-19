"""
- bisect
정렬된 리스트를 삽입 후 다시 정렬할 필요 없도록 관리할 수 있도록 지원
bisect를 이용해서 answer에 더해줄 때, 중복되는 수의 개수를 한 번에 더해줌.
- bisect_left(a, x, lo=0, hi=len(a))
리스트 a에 x를 삽입할 위치를 반환한다. 만약 리스트 a내에 이미 x가 존재하는 경우, x의 가장 왼쪽 위치 반환
import bisect

a = [1, 2, 4, 4, 6]
print(bisect.bisect_left(a, 4))  # 2
print(bisect.bisect_left(a, 3))  # 2
"""

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))
arr.sort()

"""com = combinations(arr,3)
cnt=0
for i in com:
    if sum(i)==0:
        cnt+=1
        
print(cnt)"""

from bisect import bisect_left

ans =0 

for i in range(len(arr)-2):
    left, right = i+1, n-1
    
    while left < right:
        re = arr[i]+arr[left]+arr[right]
        if re>0:
            right-=1
        else:
            if re==0:
                if arr[left]==arr[right]:
                    ans +=right-left
                else:
                    idx = bisect_left(arr,arr[right])
                    ans += right-idx+1
                    
            left+=1
print(ans)