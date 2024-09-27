'''
8
71 39 *44 -> 39
*32 83 55 -> 32
51 37 *63 -> 37
89 *29 100 -> 89
83 58 *11 -> 11
65 *13 15 -> 13
47 25 *29 -> 29
*60 66 19 -> 19
'''
import sys

input = sys.stdin.readline

n = int(input())
f = [0]*n

for i in range(n):
    f[i] = list(map(int, input().split()))
    
for i in range(1,n):
    f[i][0] = min(f[i-1][1],f[i-1][2]) + f[i][0]
    f[i][1] = min(f[i-1][0],f[i-1][2]) + f[i][1]
    f[i][2] = min(f[i-1][0],f[i-1][1]) + f[i][2]
    
print(min(f[n-1][0],f[n-1][1],f[n-1][2]))
