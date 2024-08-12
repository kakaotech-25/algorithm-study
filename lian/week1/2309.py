import itertools
ls = []
for _ in range(9):
    ls.append(int(input()))

for i in itertools.combinations(ls, 7):
    num = sum(i)
    if num == 100:
        ans = sorted(i)
        for j in range(len(ans)):
            print(ans[j])
        break