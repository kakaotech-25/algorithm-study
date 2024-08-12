n = int(input())
ls = []
ans = []
for _ in range(n):
    tmp = list(input())
    ls.append(tmp[0])
names = list(set(ls))
for i in names:
    num = ls.count(i)
    if num >= 5:
        ans.append(i)
ans.sort()
if len(ans) == 0:
    print('PREDAJA')
else:
    ans = ''.join(ans)
    print(ans)
