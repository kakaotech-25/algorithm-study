import sys

input = sys.stdin.readline

n = int(input())

answer = ''
f =[]

for i in range(n):
    f.append(list(input()))


def de(x,y,n):
    global answer
    color = f[y][x]
    
    
    for i in range(y,y+n):
        for j in range(x, x+n):
            if color != f[i][j]:
                answer +='('
                de(x,y,n//2)
                de(x+n//2,y,n//2)
                de(x,y+n//2,n//2)
                de(x+n//2, y+n//2, n//2)
                answer +=')'
                return
    answer +=color
    
de(0,0,n)

print(answer)