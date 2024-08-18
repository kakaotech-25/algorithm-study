N = int(input())
M = int(input())
ls = list(map(int, input().split()))
ls.sort()
ans = 0
start, end = 0, len(ls)-1

while start < end:
    tmp = ls[start] + ls[end]
    if tmp < M:
        start += 1
    elif tmp > M:
        end -= 1
    else:
        ans += 1
        start += 1
        end -= 1
print(ans)
