# 시간 초과
import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())
s = [tuple(map(int, input().strip().split())) for _ in range(m)]

def isEqual(a, b):
    global n
    result = True
    for i in range(n-1):
        for j in range(i, n):
            if a[i] < a[j]:
                if b[i] >= b[j]:
                    result = False
                    break
            elif a[i] == a[j]:
                if b[i] != b[j]:
                    result = False
                    break
            elif a[i] > a[j]:
                if b[i] <= b[j]:
                    result = False
                    break
        if not result:
            break
    return result

ans = []
for i in range(m-1):
    for j in range(i+1, m):
        if isEqual(s[i], s[j]):
            tmp = (sorted(s[i]), sorted(s[j]))
            if tmp not in ans:
                ans.append(tmp)

print(ans)
print(len(ans))
