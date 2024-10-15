import sys

input = sys.stdin.readline

from itertools import combinations_with_replacement

n, m =map(int,input().split())

arr = list(map(int, input().split()))

arr.sort()

re = combinations_with_replacement(arr,m)

for i in re:
    print(*i)