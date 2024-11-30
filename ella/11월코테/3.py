#이분탐색
#해설 참고
#이게 내가 알던 이분탐색?
import sys
from math import inf
input = sys.stdin.readline

# n: 배열 크기, s: 목표 합(s명 이상)
n, s = map(int, input().split())
# A: nxn 배열 입력받기(사람의 수)
A = [list(map(int, input().split())) for _ in range(n)]
# B: 임의의 부분합을 저장할 (n+1)x(n+1) 배열
B = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        B[i][j] = B[i - 1][j] + B[i][j - 1] - B[i - 1][j - 1] + A[i - 1][j - 1]


# (i1, j1)부터 (i2, j2)까지 합 반환 함수
def range_sum(i1, j1, i2, j2):
    return B[i2][j2] - B[i1 - 1][j2] - B[i2][j1 - 1] + B[i1 - 1][j1 - 1]

# kxk 정사각형 중 합이 가장 작은 값을 찾는 함수
def f(k):
    res = inf
    for i in range(1, n - k + 2):
        for j in range(1, n - k + 2):
            res = min(res, range_sum(i, j, i + k - 1, j + k - 1))
    return res

# 이분탐색
start = 1 
end = n 
res = -1 #k의 최소값

while start <= end:
    mid = (start + end) // 2
    if f(mid) >= s: 
        res = mid 
        end = mid - 1
    else:
        start = mid + 1 

print(res)