T = int(input())
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def bfs(x, y):
    q = []
    q.append([x,y])
    while len(q) != 0:
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if ls[nx][ny] == 1:
                q.append([nx, ny])
                ls[nx][ny] = 0

for _ in range(T):
    M, N, K = map(int, input().split())
    ls = [[0] * (M) for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        ls[Y][X] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if ls[i][j] == 1:
                bfs(i, j)
                ans += 1
    print(ans)
