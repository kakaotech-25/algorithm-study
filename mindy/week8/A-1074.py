import sys
input=sys.stdin.readline

n,r,c=map(int,input().split())
ans=0

def solve(x,y,n): #x,y시작점, 각 내부사각형
    global ans
    if x==r and y==c:
        print(ans)
        exit(0)
    if n==1:
        ans+=1
        return
    if not (x<=r<x+n and y<=c<y+n):
        ans+=n*n
        return
    temp=n//2
    solve(x,y,temp)
    solve(x,y+temp,temp)
    solve(x+temp,y,temp)
    solve(x+temp,y+temp,temp)

solve(0,0,2**n)
print(ans)