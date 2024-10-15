from itertools import combinations

while True:
    ls = list(map(int, input().split()))
    if ls[0] == 0:
        break
    num = ls.pop(0)
    for i in combinations(ls,6):
        ans = list(i)
        print(*ans)
    print()