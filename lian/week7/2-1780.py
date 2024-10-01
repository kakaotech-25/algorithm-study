import sys
input = sys.stdin.readline
n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
ans1 = 0
ans2 = 0
ans3 = 0

def paper(x,y,n):
    global ans1
    global ans2
    global ans3
    tmp = ls[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if tmp != ls[i][j]:
                for a in range(3):
                    for b in range(3):
                        paper(x+(n//3)*a, y+(n//3)*b, n//3)
                return
    if tmp == -1:
        ans1 += 1
    elif tmp == 0:
        ans2 += 1
    elif tmp == 1:
        ans3 += 1


paper(0,0,n)
print(ans1)
print(ans2)
print(ans3)