import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())
l = tuple(map(int, input().strip().split()))

low = 0
high = max(l)
maxlen = 0
while low <= high:
    mid = (low + high) // 2
    # print(f"{high} {mid} {low}")
    if mid != 0:
        tmp = sum(map(lambda x: x//mid, l))
        if mid > 0 and tmp >= m:
            maxlen = max(maxlen, mid)
        if tmp >= m:
            low = mid + 1
        else:
            high = mid - 1
    else:
        if high > 0 and sum(map(lambda x: x//high, l)) >= m:
            maxlen = max(maxlen, high)
        if low > 0 and sum(map(lambda x: x//low, l)) >= m:
            maxlen = max(maxlen, low)
        break

print(maxlen)