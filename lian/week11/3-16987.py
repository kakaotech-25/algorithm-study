import sys

input = sys.stdin.readline

N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def dfs(idx):
    global ans

    if idx == N:
        cnt = sum(1 for egg in ls if egg[0] <= 0)
        ans = max(ans, cnt)
        return

    if ls[idx][0] <= 0:
        dfs(idx + 1)
        return

    flag = False

    for i in range(N):
        if i != idx and ls[i][0] > 0:
            ls[idx][0] -= ls[i][1]
            ls[i][0] -= ls[idx][1]
            flag = True
            
            dfs(idx + 1)
            ls[idx][0] += ls[i][1]
            ls[i][0] += ls[idx][1]

    if not flag:
        dfs(idx + 1)
dfs(0)
print(ans)
