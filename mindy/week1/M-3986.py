# 스택 사용
# ABBA[AB][ABB][A],[AA]

import sys

input = sys.stdin.readline

n = int(input().strip())

cnt = 0
for _ in range(n):
    alpa = input().strip()
    stack=[]
    for i in alpa:
        if stack and stack[-1] ==i:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        cnt +=1

print(cnt)