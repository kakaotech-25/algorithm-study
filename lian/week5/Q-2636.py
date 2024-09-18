from collections import deque
N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
ans = 0

while True:
    visited = [[False] * M for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = True
    tmp = []

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if cheese[nx][ny] == 1:
                tmp.append((nx, ny))
            elif cheese[nx][ny] == 0:
                q.append((nx, ny))

    if not tmp:
        break

    for x, y in tmp:
        cheese[x][y] = 0
    ans = len(tmp)
    time += 1

print(time)
print(ans)
