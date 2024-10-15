# unsolved
# S: 이다솜파, Y: 임도연파
# 5*5 중 7명 선발
# 칠공주: S > Y
# 백트래킹 + DFS 
import sys
input = sys.stdin.readline
std = [list(map(str, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
answer = []
cnt = 0

def back(x, y):
    global cnt
    if len(answer) == 7:
        cntS = 0
        cntY = 0
        for a in answer:
            if a == 'S':
                cntS += 1
            else:
                cntY += 1
        if cntS > cntY:
            cnt += 1
        return
    else:
        for i in std:
            answer.append(std[i][j])
            back(i, j)
            answer.pop()

def bfs():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

back(0, 0)
print(cnt)