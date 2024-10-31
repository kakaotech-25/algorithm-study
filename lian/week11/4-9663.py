# 시간초과 남..

import sys

input = sys.stdin.readline

N = int(input())
ans = 0
ls = [[0] * N for _ in range(N)]


def check(row, col):
    for i in range(row):
        if ls[i][col] == 1:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if ls[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if ls[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def dfs(row):
    global ans

    if row == N:
        ans += 1
        return

    for col in range(N):
        if check(row, col):
            ls[row][col] = 1
            dfs(row + 1)
            ls[row][col] = 0

dfs(0)
print(ans)
