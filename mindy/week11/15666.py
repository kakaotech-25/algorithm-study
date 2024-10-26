import sys

input = sys.stdin.readline

from itertools import combinations_with_replacement

n,m = map(int,input().split())

arr = list(map(int, input().split()))

arr = set(arr)
arr =list(arr)
arr.sort()

com = combinations_with_replacement(arr,m)

for x in com:
    for i in x:
        print(i, end=" ")
    print()
