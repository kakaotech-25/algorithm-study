import sys

input = sys.stdin.readline
n = int(input())

p = [list(map(int, input().strip())) for _ in range(n)]

def dev(x, y, z):
    num = p[x][y]
    for i in range(x, x+z):
        for j in range(y, y+z):
            if num != p[i][j]:
                print("(", end="")
                for a in range(2):
                    for b in range(2):
                        dev(x + (z//2*a), y + (z//2*b), z//2)
                print(")", end="")
                return
    if num == 0:
        print("0", end="")
    elif num == 1:
        print("1", end="")

dev(0, 0, n)