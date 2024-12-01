import sys

input = sys.stdin.readline

a, b =map(int, input().split())
re = 0
if a>b:
    re +=(b+b+1)
else:
    re += (a+a-1)
    
print(re)