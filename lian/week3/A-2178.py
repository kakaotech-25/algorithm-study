N, M = map(int, input().split())
ls = [list(map(int, input())) for _ in range(N)]
visited = [[False for j in range(M)] for i in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
q = [[0,0]]
while len(q) != 0:
    x = q[0][0]
    y = q[0][1]
    q.pop(0)
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if ls[nx][ny] == 0 or visited[nx][ny]:
            continue
        visited[nx][ny] = True
        q.append([nx, ny])
        ls[nx][ny] += ls[x][y]
print(ls[N-1][M-1])