'''
3 1
r c

2  0  (1 0)
y_ x_ (i j)
'''
import sys

n, r, c = map(int, sys.stdin.readline().strip().split())
count = 0
flag = False

def s(n, x=0, y=0):
    if n == 1:
        global count
        global flag
        if y == r and x == c:
            flag = True
        # print(f"{y+1}행 {x+1}열")
        # count += 1
        return
    w = n // 2
    for i in range(2):
        y_ = y + i * w
        for j in range(2):
            x_ = x + j * w
            if x_ <= c < x_ + w and y_ <= r < y_ + w:
                # print(f"{y_} {x_}")
                # print(f"{i} {j}")
                count += (2*i+j) * w**2
                # print(count)
                s(w, x_, y_)
            if flag:
                break
        if flag:
            break
    
s(2**n)
print(count)