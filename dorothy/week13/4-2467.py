import sys
input = sys.stdin.readline
n = int(input().strip())
s = tuple(map(int,input().strip().split()))

s = tuple(sorted(s))
ans = (s[0], s[1])
v = abs(s[0]+s[1])
for idx, val in enumerate(s):
    low = idx+1
    high = n-1
    flag = False
    while low <= high:
        mid = (low + high) // 2
        tmp = val + s[mid]
        if abs(tmp) < v:
            ans = (val, s[mid])
            v = abs(tmp)
            if tmp == 0:
                flag = True
                break
        if tmp > 0:
            high = mid - 1
        elif tmp < 0:
            low = mid + 1
    
    if flag:
        break

print(*ans)