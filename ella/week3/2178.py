from collections import deque

n, m = map(int, input().split())

maze = []

for i in range(n):
    maze.append(list(map(int, input())))

def bfs(x, y):
    #상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        #상하좌우 결과
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>=0 and ny>=0 and nx<n and ny<m:
                if maze[nx][ny] == 1: #이동할 수 있는 경우
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))
                    
bfs(0, 0)
print(maze[n-1][m-1])
