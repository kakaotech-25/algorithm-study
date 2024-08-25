N = int(input())
ls = [list(map(int, input())) for _ in range(N)]
ans = []

def quadtree(x,y,N):
    tmp = ls[x][y]
    d = N//2
    for i in range(x, x+N):
        for j in range(y, y+N):
            if tmp != ls[i][j]:
                ans.append('(')
                quadtree(x,y,d)
                quadtree(x,y+d,d)
                quadtree(x+d,y,d)
                quadtree(x+d,y+d,d)
                ans.append(')')
                return
    ans.append(str(tmp))

quadtree(0,0,N)
print(''.join(ans))