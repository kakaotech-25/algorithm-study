import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))

arr  = sorted(set(num))

dic = {arr[i]:i for i in range(len(arr))}

for i in num:
    print(dic[i],end=' ')