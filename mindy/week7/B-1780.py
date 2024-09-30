'''import sys

input = sys.stdin.readline

# 기저값 , 1일때는 탐색을 하지 않고 계산후 종료시키지
# 설정한 사이즈에 대해 같은 값을 가지는지 확인
# 
n = int(input())
p=[list(map(int, input().split())) for _ in range(n)]
f =[]



def re(x,y,n):
    color = p[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != p[i][j]:
                for a in range(3):
                    for b in range(3):
                        re(x+(n//3)*a, y+(n//3)*b, n//3)
                return
    if color == 1:
        f.append(1)
    elif color ==-1:
        f.append(-1)
    else:
        f.append(0)
re(0,0,n)'''
import sys


def dfs(x, y, z):
    global answer
    visited = graph[x][y]

    # 반복문을 통해 종이를 확인
    for i in range(x, x + z):
        for j in range(y, y + z):
            # 시작점에 종이의 수가 현재 종이의 수와 다르다면
            if graph[i][j] != visited:
                # 3 * 3 범위를 재귀적으로 탐색
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * z // 3, y + l * z // 3, z // 3)
                return

    # 카운트
    if visited == -1:
        answer[0] += 1
    elif visited == 0:
        answer[1] += 1
    else:
        answer[2] += 1


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [0, 0, 0]
dfs(0, 0, n)
[print(res) for res in answer]
