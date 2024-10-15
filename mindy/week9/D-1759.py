import sys

from itertools import combinations

input = sys.stdin.readline

l, c = map(int, input().split())

arr = list(map(str, input().split()))

arr.sort()
re = combinations(arr, l)

ans = []

for alpa in re:
    c_count=0
    v_count=0
    
    for i in alpa:
        if i in 'aeiou':
            c_count +=1
        else:
            v_count +=1
            
    if c_count>=1 and v_count >=2:
        print(''.join(alpa))
    
