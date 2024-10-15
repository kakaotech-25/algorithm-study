import sys
from itertools import combinations
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ls = [list(input().strip()) for _ in range(5)]
check = [(i, j) for i in range(5) for j in range(5)]
ans = 0

for i in combinations(check, 7):
    cnt_s = 0
    for x, y in i:
        if ls[x][y] == 'S':
            cnt_s += 1

    if cnt_s >= 4:
        visited = [[False] * 5 for _ in range(5)]
        q = deque([i[0]])
        visited[i[0][0]][i[0][1]] = True
        cnt = 1

        while q:
            x, y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    continue
                if (nx, ny) not in i:
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1

        if cnt == 7:
            ans += 1

print(ans)
