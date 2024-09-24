import sys
input = sys.stdin.readline
n = int(input())
f = [0] * 1000001
f[0] = 1
f[1] = 2
for i in range(2,n):
    f[i] = (f[i-1]+f[i-2])%15746
print(f[n-1])