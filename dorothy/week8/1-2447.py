import sys
n = int(sys.stdin.readline().strip())
stars = [["*"]*n for _ in range(n)]

def s(n, x=0, y=0):
    if n == 0:
        return
    w = n//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                x_ = x + w
                y_ = y + w
                for k in range(x_, x_ + w):
                    for l in range(y_, y_ + w):
                        stars[l][k] = " "
            else:
                s(w, x + i * w, y + j * w)

s(n)
for s in stars:
    print("".join(s))