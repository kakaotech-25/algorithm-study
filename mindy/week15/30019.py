# https://www.acmicpc.net/contest/view/1120
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
dic ={}

for i in range(m):
    arr =list(map(int,input().split()))

    if arr[0] not in dic:
        dic[arr[0]] = [arr[1],arr[2]]
        print("YES")
    else:
        if dic[arr[0]][1] > arr[1]:
            print('NO')
        else:
            dic[arr[0]] = [arr[1],arr[2]]
            print('YES')
