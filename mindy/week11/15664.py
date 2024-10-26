import sys

input = sys.stdin.readline

from itertools import combinations

n, m = map(int, input().split())

arr= list(map(int,input().split()))
arr.sort()

com = combinations(arr,m)
com = set(com)
com = list(com)
com.sort()
ans = []

for x in com:
    for i in x:
        print(i, end=" ")
    print()