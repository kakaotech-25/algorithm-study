import sys

n, m = map(int, sys.stdin.readline().strip().split())
woods = map(int, sys.stdin.readline().strip().split())

woods = sorted(woods)
h = 0
cm = sum(woods)

low = 0
high = max(woods)
while low <= high:
    mid = (low + high) // 2
    tmp1 = sum(map(lambda x: x-mid if x-mid > 0 else 0, woods))
    if m <= tmp1:
        if cm > tmp1:
            cm = tmp1
            h = max(h, mid)
            # print(tmp1)
    if tmp1 < m:
        high = mid - 1
    elif tmp1 > m:
        low = mid + 1
    else:
        break


print(h)
