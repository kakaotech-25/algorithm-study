from itertools import combinations

N, S = map(int, input().split())
ls = list(map(int, input().split()))
ans = 0
while(N>0):
    for i in combinations(ls, N):
        tmp = sum(list(i))
        if tmp == S:
            ans += 1
    N -= 1
print(ans)