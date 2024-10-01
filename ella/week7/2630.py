# 1780.py랑 똑같이 풀었는데 이건 맞음.. 다른점이 뭐지??
import sys

input = sys.stdin.readline
n = int(input())

p = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0]

def dev(x, y, z):
    global answer
    color = p[x][y]
    for i in range(x, x+z):
        for j in range(y, y+z):
            if color != p[i][j]:
                for a in range(2):
                    for b in range(2):
                        dev(x + (z//2*a), y + (z//2*b), z//2)
                return
    if color == 0:
        answer[0] += 1
    elif color != 0:
        answer[1] += 1

dev(0, 0, n)
print(answer[0])
print(answer[1])