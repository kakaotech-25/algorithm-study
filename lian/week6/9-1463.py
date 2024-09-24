import sys
input = sys.stdin.readline
N = int(input())
f = [0] * 10000001
for i in range(2, N+1):
    f[i] = f[i-1] + 1
    if i % 2 == 0:
        f[i] = min(f[i], f[i//2] + 1)
    if i % 3 == 0:
        f[i] = min(f[i], f[i//3] + 1)
print(f[N])