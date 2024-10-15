'''
7명의 여학생
7명의 자리 서로 인접
이다솜파(4명이상) + 임도연파

접근법
bfs로 전부 탐색
뎁스는 7개까지만
7개에 도달했을 경우 경로의 s 개수가 4 이상이면 count += 1
'''
import sys
from collections import deque
from itertools import combinations

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

seat = [sys.stdin.readline().strip() for _ in range(5)]
route = [[False]*5 for _ in range(5)]
cnt = 0

coordinate = [(x, y) for x in range(5) for y in range(5)]
candidate = combinations(coordinate, 7)

def countS(c):
    cnt = 0
    for x, y in c:
        if seat[y][x] == 'S':
            cnt += 1
    return cnt

for c in candidate:
    if countS(c) >= 4:
        q = deque()
        # route = deque()
        visited = [[False]*5 for _ in range(5)]
        q.append((0, 0, 0))

        while q:
            x, y, depth = q.popleft()
            if depth == 7:
                cnt += 1
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    continue
                elif visited[ny][nx]:
                    continue
                
                visited[ny][nx] = True
                q.append((nx, ny))

print(cnt)