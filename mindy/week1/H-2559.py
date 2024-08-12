n, k = map(int,input().split())
a = list(map(int, input().split()))

result = []
result.append(sum(a[:k]))

for i in range(n - k):
    result.append(result[i] - a[i] + a[k+i])
        
print(max(result))