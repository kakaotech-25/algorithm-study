from collections import Counter
N = int(input())
ls = list(map(int, input().split()))
ls.sort()
M = int(input())
check = list(map(int, input().split()))
ans = Counter(ls)
for i in check:
    if i in ans:
        print(ans[i], end=' ')
    else:
        print('0', end=' ')