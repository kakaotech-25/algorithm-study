A = int(input())
ls = list(map(int, input().split()))
ans = [-1] * A
stack = []

for idx in range(A):
    while stack and ls[stack[-1]] < ls[idx]:
        ans[stack.pop()] = ls[idx]
    stack.append(idx)
print(*ans)