'''
w(1, 1, 1)
= w(0, 1, 1) + w(0, 0, 1) + w(0, 1, 0) - w(0, 0, 0)
= 1 + 1 + 1 - 1
= 2


w(2, 2, 2)
= w(1, 2, 2) + w(1, 1, 2) + w(1, 2, 1) - w(1, 1, 1)
= w(0, 2, 2) + w(0, 1, 2) + w(0, 2, 1) - w(0, 1, 1)
 + w(0, 1, 2) + w(0, 0, 2) + w(0, 1, 1) - w(0, 0, 1)

w(1, 2, 3)
= w(1, 2, 2) + w(1, 1, 2) - w(1, 1, 3)

a=0 -> 1
a=1 -> 2^1-1 + 1 = 2
a=2 -> 2^2-1 + 2 = 6
'''
import sys

a, b, c = map(int, sys.stdin.readline().strip().split())


for i in range(21):
    for j in range(21):
        for k in range(21):
            if i <= 0 or j <= 0 or k <= 0:
                