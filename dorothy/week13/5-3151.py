# 시간 초과
from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input().strip())
s = tuple(map(int, input().strip().split()))
s = sorted(s)
ans = 0
# print(s)

for i in range(n-2):
    for j in range(i+1, n-1):
        low = j+1
        high = n-1
        while low <= high:
            mid = (low+high)//2
            tmp = s[i] + s[j] + s[mid]
            if tmp == 0:
                ans += 1
                idx = mid + 1
                # print((s[i], s[j], s[mid]))
                while idx < n and s[mid] == s[idx]:
                    ans += 1
                    idx += 1
                    # print((s[i], s[j], s[mid]))
                idx = mid - 1
                while idx > j and s[mid] == s[idx]:
                    ans += 1
                    idx -= 1
                    # print((s[i], s[j], s[mid]))
                break
            elif tmp < 0:
                low = mid + 1
            elif tmp > 0:
                high = mid - 1

print(ans)