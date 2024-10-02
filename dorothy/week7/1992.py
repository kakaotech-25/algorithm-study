import sys
N = int(sys.stdin.readline().strip())
matrix = [sys.stdin.readline().strip() for _ in range(N)]


def s(x, y, w):
    flag = False
    for i in range(x, x+w):
        for j in range(y, y+w):
            if matrix[x][y] != matrix[i][j]:
                flag = True
                break
        if flag:
            break
    
    if flag:
        s_list = []
        for i in range(2):
            for j in range(2):
                s_list.append(s(x + w // 2 * i, y + w // 2 * j, w // 2))
        # print(f"{s_list}, {w}")
        return f'({"".join(s_list)})'
    else:
        return matrix[x][y]


print(f'{s(0, 0, N)}')
