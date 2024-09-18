from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
viruses = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]

for walls in combinations(empty, 3):
    tmp_lab = copy.deepcopy(lab) #독립적인 복사본 생성

    for x, y in walls:
        tmp_lab[x][y] = 1

    q = deque(viruses)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if tmp_lab[nx][ny] != 0:
                continue
            tmp_lab[nx][ny] = 2
            q.append((nx, ny))

    tmp = 0
    for i in range(N):
        for j in range(M):
            if tmp_lab[i][j] == 0:
                tmp += 1
    ans = max(ans, tmp)

print(ans)
