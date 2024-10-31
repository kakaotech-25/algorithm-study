import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

arr.sort()

def back(s):
    tmp = 0
    if len(answer) == m:
            print(" ".join(map(str, answer)))
            return
    for i in range(s, n):
        if (len(answer) == 0 or arr[i] >= answer[-1]) and tmp != arr[i]:
            tmp = arr[i]
            answer.append(arr[i])
            back(i+1)
            answer.pop()
back(0)