from collections import deque

def bfs(x, y, loc, m, n):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))
    loc[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < m and ny < n:
                if loc[nx][ny] == 1:  # 배추 위치
                    loc[nx][ny] = 0
                    queue.append((nx, ny))

t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())  # 행, 열, 배추 개수
    loc = [[0 for _ in range(n)] for _ in range(m)]
    count = 0
    for j in range(k):
        lx, ly = map(int, input().split())
        loc[lx][ly] = 1
    for a in range(m):
        for b in range(n):
            if loc[a][b] == 1:
                bfs(a, b, loc, m, n)
                count += 1
    print(count)
