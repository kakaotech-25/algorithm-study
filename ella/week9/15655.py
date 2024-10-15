#백로그
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

arr.sort()

def back():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    else:
        for i in arr:
            if i not in answer and (len(answer) == 0 or i > answer[-1]):
                answer.append(i)
                back()
                answer.pop()
back()