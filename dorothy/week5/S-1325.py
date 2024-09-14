'''
이거 실버 맞나요?ㅋㅋㅋ
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
graph = dict()
for i in range(N):
    graph[i + 1] = []

for i in range(1, M + 1):
    A, B = map(int, data[i].split())
    graph[B].append(A)

memo = {}

def dfs(node, depth_list):
    if node in memo:
        return memo[node]
    
    if len(graph[node]) == 0:
        return depth_list

    max_len = 0
    max_route = []

    for next_node in graph[node]:
        if next_node not in depth_list:
            route = dfs(next_node, depth_list + [next_node])
            if max_len < len(route):
                max_route = route
                max_len = len(route)

    memo[node] = max_route
    return max_route

max_len = 0
max_list = []

for i in range(1, N + 1):
    route = dfs(i, [i])
    if max_len < len(route):
        max_len = len(route)
        max_list = [i]
    elif max_len == len(route):
        max_list.append(i)

print(" ".join(map(str, sorted(max_list))))
