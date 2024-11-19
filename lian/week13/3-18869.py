import sys
input = sys.stdin.readline
M, N = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(M)]
res = []

    # 시간초과..
    # for i in ls:
    #     sorted_tmp = sorted(set(i))
    #     tmp = []
    #     for num in i:
    #         low, high = 0, len(sorted_tmp) - 1
    #         while low <= high:
    #             mid = (low + high) // 2
    #             if sorted_tmp[mid] < num:
    #                 low = mid + 1
    #             elif sorted_tmp[mid] > num:
    #                 high = mid - 1
    #             else:
    #                 tmp.append(mid)
    #                 break
    #     res.append(tuple(tmp))

for i in ls:
    unique = {val: idx for idx, val in enumerate(sorted(set(i)))}
    tmp = [unique[num] for num in i]
    res.append(tuple(tmp))

ans = 0
cnt = {}
for i in res:
    if i in cnt:
        ans += cnt[i]
        cnt[i] += 1
    else:
        cnt[i] = 1
print(ans)