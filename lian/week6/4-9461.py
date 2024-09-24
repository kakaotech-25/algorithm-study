import sys
input = sys.stdin.readline
T = int(input())
f = [0] * 101
for _ in range(T):
    n = int(input())
    f[0] = 1
    f[1] = 1
    f[2] = 1
    for i in range(3, n):
        f[i] = f[i-3] + f[i-2]
    print(f[n-1])