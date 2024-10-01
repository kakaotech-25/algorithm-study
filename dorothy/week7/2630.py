import sys

N = int(sys.stdin.readline().strip())
paper = [sys.stdin.readline().strip().split() for _ in range(N)]

def s(x, y, w):
    flag = False
    p1, p2 = 0, 0
    for i in range(x, x+w):
        for j in range(y, y+w):
            if paper[i][j] != paper[x][y]:
                flag = True
                break
        if flag:
            break

    if flag:
        for i in range(2):
            for j in range(2):
                np1, np2 = s(x + i * w // 2, y + j * w // 2, w // 2)
                p1, p2 = p1 + np1, p2 + np2
    else:
        if paper[i][j] == '0':
            p1 += 1
        else:
            p2 += 1
    
    return p1, p2

print("\n".join(map(str, s(0, 0, N))))