tc = int(input())
for _ in range(tc):
    n = int(input())
    dic = {}
    for _ in range(n):
        name, type = map(str, input().split())
        if type in dic:
            dic[type] += 1
        else:
            dic[type] = 1
    ans = 1
    for i in dic:
        ans *= dic[i]+1
    print(ans-1)