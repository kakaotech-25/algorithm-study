import sys
from collections import deque

a = (1, deque())
b = (2, deque())
c = (3, deque())
path = []

def move(f, t):
    path.append(f"{f[0]} {t[0]}")
    tmp = f[1].pop()
    t[1].append(tmp)

def s(N, f, temp, t):
    if N == 1:
        move(f, t)
        return 1
    a1 = s(N-1, f, t, temp)
    move(f, t)
    s(N-1, temp, f, t)
    return a1 * 2 + 1

N = int(sys.stdin.readline().strip())
for i in reversed(range(N)):
    a[1].append(i)

print(s(N, a, b, c))
print("\n".join(path))
