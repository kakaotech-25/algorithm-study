import sys

[a, b, c] = map(int, sys.stdin.read().splitlines())
multi = lambda a, b, c : a * b * c

result = multi(a, b, c)

arr = [0 for _ in range(10)]
for i in str(result):
    arr[int(i)] += 1

for i in arr:
    print(i)
    
