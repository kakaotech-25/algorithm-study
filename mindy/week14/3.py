# 어려워요ㅜ
import sys
from math import inf

input = sys.stdin.readline

def range_sum(i1,j1,i2,j2):
	return arr[i2][j2] - arr[i1-1][j2] - arr[i2][j1-1] + arr[i1-1][j1-1]

def f(k):
	res = inf
	for i in range(1,n-k+2):
		for j in range(1,n-k+2):
			res = min(res, range_sum(i,j,i+k-1, j+k-1))
	return res

n,s = map(int,input().split())

arr1 = [list(map(int,input().split())) for _ in range(n)]

arr = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
	for j in range(1,n+1):
		arr[i][j] = arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1] + arr1[i-1][j-1]

		
start =1
end = n
res = -1

while start <=end:
	mid = (start + end)//2
	if f(mid)>=s:
		res = mid
		end = mid-1
	else:
		start = mid +1
		
print(res)