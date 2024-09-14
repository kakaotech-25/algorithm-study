'''
모두 녹아 없어지는 데 걸리는 시간
전부 녹기 한 시간 전 치즈 개수

1: 판 세로 가로
2~: 판

무한루프(치즈가 0개 될 때까지)
    치즈 개수 세서 0개면 탈출
    공기와 접촉하지 않는 구멍 좌표를 리스트에 저장(bfs)
        q에 좌표를 넣을 때마다 area 배열에 영역의 좌표를 저장
        bfs 진행하면서 바깥 경계(테두리 혹은 좌표를 벗어나는 경우)에 해당하는 좌표를 만날 경우, is_wrapped 플래그를 False로 변경하고 일단 전부 방문(visited 표시하기 위함)
        area 배열의 요소는 is_wrapped가 True일 때만 hole_in_cheese 리스트에 좌표를 추가
    (공기에 닿은 치즈 부분을 세는 부분은 bfs 쓰지 않아도 풀릴 듯?)
    치즈 영역을 순회하면서, 주변에 공기가 있고 그 공기가 hole_in_cheese에 들어있지 않으면 해당 영역을 c 배열에 넣음
    c 배열에 담긴 좌표를 방문하여 값을 0으로 만든다
    현재 치즈의 양을 prev에 기록하고 시간을 1 카운트한다
'''
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())

map = [input().split() for _ in range(N)]
prev = 0
hour = 0

while True:
    cheese = []
    

    for i in range(N):
        for j in range(M):
            if map[i][j] == '1':
                cheese.append((j, i))
    
    len_cheese = len(cheese)
    if len_cheese == 0:
        break
    
    # 치즈에 둘러싸인 구멍을 체크
    hole_in_cheese = []
    visited = [[False] * M for _ in range(N)]
    q = deque()
    
    for y in range(N):
        for x in range(M):
            if map[y][x] == '0' and not visited[y][x]:
                area = [(x, y)]
                is_wrapped = True
                q.append((x, y))
                while q:
                    qx, qy = q.popleft()

                    for i in range(4):
                        nx, ny = (qx + dx[i], qy + dy[i])

                        # nx, ny가 테두리 영역이면 해당 영역은 공기로 파악
                        if nx < 1 or nx >= M - 1 or ny < 1 or ny >= N - 1:
                            is_wrapped = False
                            continue
                        elif visited[ny][nx]:
                            continue

                        if map[ny][nx] == "0":
                            q.append((nx, ny))
                            visited[ny][nx] = True
                            area.append((nx, ny))
                # print(area)
                if is_wrapped:
                    hole_in_cheese = hole_in_cheese + area

    # print(hole_in_cheese)
    
    # 공기에 닿은 치즈 영역을 담을 리스트
    c = []
    q.clear()
    visited = [[False] * M for _ in range(N)]

    # 모든 치즈 칸을 검사
    for i in cheese:
        if visited[i[1]][i[0]]:
            continue
        q.append(i)

        while q:
            x, y = q.popleft()

            for k in range(4):
                nx, ny = (x + dx[k], y + dy[k])

                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue
                elif visited[ny][nx]:
                    continue
                
                if map[ny][nx] == '0' and (nx, ny) not in hole_in_cheese:
                    c.append((x, y))
                    break
                elif map[ny][nx] == '1':
                    q.append((nx, ny))
                    visited[ny][nx] = True
 
    for coordinate in c:
        x, y = coordinate
        map[y][x] = '0'
    
    # print(c)
    prev = len_cheese
    hour += 1
    
    # if hour == 2:
    #     for row in map:
    #         print(row)

print(hour)
print(prev)
        