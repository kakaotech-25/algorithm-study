# 백로그
import sys
input = sys.stdin.readline
n = int(input())

p = [list(map(int, input().split())) for _ in range(n)]

answer = [0,0,0]

def det(x, y, z):
    global answer
    num = p[x][y]
    for i in range(x, x+z):
        for j in range(y, y+z):
            if num != p[i][j]:
                for a in range(3):
                    for b in range(3):
                        det(x + (z//3*a), y + (z//3*b), z//3)
                return # 종이에 채워진 숫자가 달라 9개로 자르고 종료

    # 종이에 채워진 숫자가 모두 같은 경우    
    if num == -1:
        answer[0] += 1
    elif num == 0:
        answer[1] += 1
    else:
        answer[2] += 1

det(0, 0, n)
print(answer[0])
print(answer[1])
print(answer[2])