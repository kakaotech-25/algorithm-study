import sys
input = sys.stdin.readline

A, B = map(int, input().split())

minValue = min(A, B)

result = 0
if A > B :
    result = minValue * 2 + 1
else :
    result = minValue * 2 - 1

print(result)
