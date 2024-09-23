import sys
input = sys.stdin.readline

t = int(input())


f = [0] *101
for _ in range(t):
    n  = int(input())
    f[1] =1
    f[2]=1
    f[3]=1
    for i in range(4,n+1):
        f[i] = f[i-2]+f[i-3]
    print(f[n])
    