import sys

N = int(sys.stdin.readline().strip())
paper = [sys.stdin.readline().strip().split() for _ in range(N)]

def s(x, y, w):
    p1, p2, p3 = 0, 0, 0
    flag = False
    for i in range(x, x + w):
        for j in range(y, y + w):
            if paper[i][j] != paper[x][y]:
                flag = True
                break
        if flag:
            break
    
    if flag:
        for k in range(3):
            for l in range(3):
                np1, np2, np3 = s(x + k * w // 3, y + l * w // 3, w // 3)
                p1, p2, p3 = np1 + p1, np2 + p2, np3 + p3
    else:
        if paper[x][y] == '-1':
            p1 += 1
        elif paper[x][y] == '0':
            p2 += 1
        else:
            p3 += 1
    
    return p1, p2, p3

print("\n".join(map(str, s(0, 0, N))))

