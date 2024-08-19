from string import ascii_lowercase

n = list(input())
ls = list(ascii_lowercase)
ans = [0 for _ in range(len(ls))]
for i in n:
    num = ls.index(i)
    ans[num] += 1
print(*ans)