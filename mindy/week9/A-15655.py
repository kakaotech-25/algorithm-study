import sys
from itertools import combinations

input = sys.stdin.readline

n, m =map(int, input().split())

arr= list(map(int,input().split()))

# n개의 자연수 중에서 수열을 만드는것
arr.sort()
re = combinations(arr,m)

for i in re:
    print(*i)