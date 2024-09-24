n = int(input())
ls = list(map(int, input().split()))
for i in range(1, n):
    ls[i] = max(ls[i], ls[i]+ls[i-1])
print(max(ls))