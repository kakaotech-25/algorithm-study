N = int(input())
ans = 0
for _ in range(N):
    ls = list(input())
    stk = []
    if not len(stk):
        stk.append(ls.pop(0))
    for i in range(len(ls)):
        if len(stk) == 0 or stk[-1] != ls[i]:
            stk.append(ls[i])
        else:
            stk.pop()
    if not len(stk):
        ans += 1
print(ans)
