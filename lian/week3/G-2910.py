N, C = map(int, input().split())
ls = list(map(int, input().split()))
dic = {}
for i in ls:
    if not i in dic:
        dic[i] = 1
    else:
        dic[i] += 1
tmp = sorted(dic.items(), key=lambda x: x[1], reverse = True)
ans = []
for i, j in tmp:
    for _ in range(j):
        print(i, end=' ')
