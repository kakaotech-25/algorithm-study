import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

M, N, K = map(int, input().split())
ls = [[0] * N for _ in range(M)]
ans = []

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    ls[x][y] = 1
    tmp = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if (0 <= nx < M) and (0 <= ny < N) and ls[nx][ny] == 0:
            if ls[nx][ny] == 0:
                tmp += dfs(nx, ny)
    return tmp

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            ls[j][i] = 1

for i in range(M):
    for j in range(N):
        if ls[i][j] == 0:
            ans.append(dfs(i,j))
print(len(ans))
print(*sorted(ans))