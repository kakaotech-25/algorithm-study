# 도저히 못풀겠어요.
import sys
input = sys.stdin.readline
from math import ceil, log2


def init(node, start, end):
    if start == end: 
        tree[node] = A[start] 
    else:
        mid = (start + end) // 2 
        init(node * 2, start, mid) 
        init(node * 2 + 1, mid + 1, end) 
        tree[node] = tree[node * 2] + tree[node * 2 + 1] 


def update(node, start, end, idx, val):
    if idx < start or end < idx: 
        return 
    tree[node] += val 
    if start != end: 
        mid = (start + end) // 2 
        update(node * 2, start, mid, idx, val) 
        update(node * 2 + 1, mid + 1, end, idx, val) 


def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_sum = query(node * 2, start, mid, left, right) 
    right_sum = query(node * 2 + 1, mid + 1, end, left, right); 
    return left_sum + right_sum

N, Q = map(int, input().split())
A = list(map(int, input().split()))


M = 2 ** ceil(log2(N) + 1) 
tree = [0] * M


init(1, 0, N - 1)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1: 
        l = q[1] - 1
        r = q[2] - 1
        print(query(1, 0, N - 1, l, r))
    elif q[0] == 2: 
        i = q[1] - 1
        x = q[2]
        update(1, 0, N - 1, i, x) 
    else: 
        i = q[1] - 1
        x = q[2]
        update(1, 0, N - 1, i, -x) 