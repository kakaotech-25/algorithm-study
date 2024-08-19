N, K = map(int, input().split())
ls = list(map(int, input().split()))
ans = sum(ls[0:K])
tmp = sum(ls[0:K])
for i in range(N-K):
    tmp -= ls[i]
    tmp += ls[K+i]
    ans = max(ans, tmp)
print(ans)