'''
1: 트리의 노드의 개수 N
2: 0 ~ N-1 노드의 부모 노드가 주어진다.
3: 지울 노드의 번호

* 삽질주의 힌트
root는 0이 아닐 수 있음
이진 트리가 아닐 수 있음
'''
from collections import deque

def delete_node(parent_nodes, node, tree):
    if node not in tree:
        return
    
    for child in tree[node].copy():
        delete_node(parent_nodes, child, tree)
    
    tree[parent_nodes[node]].remove(node)
    tree.pop(node)

def count_leaf():
    N = int(input())
    parent_nodes = list(map(int, input().split()))

    tree = dict()
    for child, parent in enumerate(parent_nodes):
        if parent in tree:
            tree[parent].append(child)
        else:
            tree[parent] = [child]
        if child not in tree:
            tree[child] = []

    # print(tree)
    deleted_node = int(input())
    # 루트 노드를 삭제했다면 함수 탈출
    if deleted_node == tree[-1][0]:
        return 0

    # 노드 삭제
    delete_node(parent_nodes, deleted_node, tree)

    # print(tree)
    # q = deque()
    # for i in tree[-1]:
    #     q.append(i)

    # 리프 노드 탐색
    leaf = 0
    # while q:
    #     node = q.popleft()
        
    #     if node in tree and len(tree[node]) > 0:
    #         for child in tree[node]:
    #             q.append(child)
    #     else:
    #         leaf += 1
    for child_nodes in tree.values():
        if len(child_nodes) == 0:
            leaf += 1
    
    return leaf

print(count_leaf())