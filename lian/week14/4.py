# 1 l r = l ~ r 번 잡초의 크기 합
# 2 i x = i번 잡초가 x 만큼 증가
# 3 i x = i번 잡초가 x 만큼 감소

import sys
input = sys.stdin.readline
N, Q = map(int, input().split()) # N = 잡초의 개수, Q = 쿼리의 개수
ls = list(map(int, input().split())) # 잡초들 초기 길이

from math import ceil, log2
# 초기화
def init(node, start, end):
	if start == end:
		tree[node] = ls[start]
	else:
		mid = (start+end)//2
		init(node*2, start, mid)
		init(node*2+1, mid+1, end)
		tree[node] = tree[node*2]+tree[node*2+1]

#구간합	
def query(node, start, end, left, right):
	if right < start or end < left:
		return 0
	if left <= start and end <= right:
		return tree[node]
	mid = (start+end)//2
	left_sum = query(node*2, start, mid, left, right)
	right_sum = query(node*2+1, mid+1, end, left, right)
	return left_sum + right_sum

#값 업데이트
def update(node, start, end, idx, diff):
	if idx < start or idx > end:
		return
	tree[node] += diff
	if start != end:
		mid = (start+end)//2
		update(node*2, start, mid, idx, diff)
		update(node*2+1, mid+1, end, idx, diff)
	
tree_size = 2**ceil(log2(N)+1)
tree = [0]*tree_size
init(1,0,N-1)

for _ in range(Q):
	num,x,y = map(int, input().split())
	if num == 1:
		print(query(1,0,N-1,x-1,y-1))
	elif num == 2:
		idx = x-1
		update(1,0,N-1,idx,y)
	elif num == 3:
		idx = x-1
		update(1,0,N-1,idx,-y)
	