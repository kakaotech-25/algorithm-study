'''
0: 빈칸
1: 벽
2: 바이러스

N, M = 세로, 가로

안전 영역이 제일 큰 경우의 넓이를 구하시오.
'''
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
map = [input().split() for _ in range(N)]
empty_space = []
wall = []
virus = []

for y in range(N):
    for x in range(M):
        if map[y][x] == '0':
            empty_space.append((x, y))
        elif map[y][x] == '1':
            wall.append((x, y))
        else:
            virus.append((x, y))
        

len_empty_space = len(empty_space)
max_area = 0
for i in range(len_empty_space - 2):
    for j in range(i + 1, len_empty_space - 1):
        for k in range(j + 1, len_empty_space):
            n_wall = (empty_space[i], empty_space[j], empty_space[k])
            # print(empty_space[i])
            n_virus = []

            q = deque()
            visited = [[False] * M for _ in range(N)]

            for v in virus:
                q.append(v)

                while q:
                    x, y = q.popleft()

                    for l in range(4):
                        nx, ny = (x + dx[l], y + dy[l])
                        
                        if nx < 0 or nx >= M or ny < 0 or ny >= N:
                            continue
                        elif visited[ny][nx] or (nx, ny) in n_virus or (nx, ny) in n_wall:
                            continue

                        if map[ny][nx] == '0':
                            n_virus.append((nx, ny))
                            visited[ny][nx] = True
                            q.append((nx, ny))
            
            cnt = 0
            for e in empty_space:
                if e in n_wall or e in n_virus or e in wall or e in virus:
                    continue
                else:
                    cnt += 1
            
            max_area = max(max_area, cnt)

            # print(f"empty: {empty_space}")
            # print(f"n_wall: {n_wall}")
            # print(f"n_virus: {n_virus}")
            # print("")



print(max_area)
            
            