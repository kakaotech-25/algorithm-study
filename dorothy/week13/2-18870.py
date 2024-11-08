import sys
input = sys.stdin.readline

n = int(input().strip())
x = tuple(map(int, input().strip().split()))

sorted_x = sorted(set(x))
x_ = []
l = len(sorted_x)

for i in x:
    low = 0
    high = l-1
    idx = 0 
    while low <= high:
        mid = (low + high) // 2
        if i > sorted_x[mid]:
            idx = mid
            low = mid + 1
        elif i < sorted_x[mid]:
            high = mid - 1
        else:
            idx = mid
            break
    x_.append(idx)

print(*x_)