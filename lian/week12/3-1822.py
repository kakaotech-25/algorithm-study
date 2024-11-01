# import sys
# input = sys.stdin.readline
#
# a, b = map(int, input().split())
# A = list(map(int, input().split()))
# B = sorted(map(int, input().split()))
# ans = []
# for num in A:
#     low, high = 0, len(B)-1
#     flag = 1
#     while low <= high:
#         mid = (low+high)//2
#         if num < B[mid]:
#             high = mid-1
#         elif num > B[mid]:
#             low = low+1
#         else:
#             flag = 0
#             break
#     if flag:
#         ans.append(num)
# print(len(ans))
# if len(ans):
#     print(*sorted(ans))

# 시간초과를 도무지 해결할 수가 없음

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

ans = sorted(A - B)

print(len(ans))
if len(ans):
    print(*ans)
