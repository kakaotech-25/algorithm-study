import sys
input = sys.stdin.readline

N = input().strip()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# print(N)
# print(a)
# print(b)

diff = 0
for index, el in enumerate(a):
   diff += abs(a[index] - b[index]) 

print(int(diff / 2))