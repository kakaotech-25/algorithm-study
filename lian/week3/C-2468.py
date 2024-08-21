N = int(input())
arr = []
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
for _ in range(N):
    arr.append(list(map(int, input().split())))
ans = []

# 가장 높은 지점을 찾는다
maxnum = 0
for i in range(N):
    for j in range(N):
        if maxnum < arr[i][j]:
            maxnum = arr[i][j]

ans = 1 #비가 아예 안 올 수 있으므로 최소 안전영역은 1
for h in range(1,maxnum+1): # 물에 잠기는 높이
    step_ans = 0
    visited = [[False for j in range(N)] for i in range(N)] #이미 본 곳을 체크하기 위해
    for i in range(N):
        for j in range(N):

            # 물에 잠긴 경우 + 이미 본 경우
            if arr[i][j] <= h or visited[i][j]:
                continue

            # 물에 안 잠긴 경우
            step_ans += 1
            q = []
            q.append([i,j])
            visited[i][j] = True
            while len(q) != 0:
                x = q[0][0]
                y = q[0][1]
                q.pop(0)
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if arr[nx][ny] <= h or visited[nx][ny]:
                        continue
                    visited[nx][ny] = True
                    q.append([nx, ny])

    ans = max(ans, step_ans)
print(ans)