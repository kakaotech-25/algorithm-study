n =int(input())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
    

def check(x,y,n):
    for i in range(x, x+n):
        for j in range(y,y+n):
            if graph[x][y] != graph[i][j]:
                print("(", end="")
                check(x,y,n//2)
                check(x,y+n//2,n//2)
                check(x+n//2,y,n//2)
                check(x+n//2,y+n//2,n//2)
                print(")",end="")
                return
    print(1 if graph[x][y]==1 else 0, end="")

check(0,0,n)