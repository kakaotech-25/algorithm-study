import sys
input = sys.stdin.readline

N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0
def paper(x,y,N):
    global white
    global blue
    tmp = ls[x][y]
    d = N//2
    for i in range(x, x+N):
        for j in range(y, y+N):
            if tmp != ls[i][j]:
                paper(x, y, d)
                paper(x, y+d, d)
                paper(x+d, y, d)
                paper(x+d, y+d, d)
                return
    if tmp == 0:
        white += 1
    elif tmp == 1:
        blue += 1
paper(0,0,N)
print(white)
print(blue)