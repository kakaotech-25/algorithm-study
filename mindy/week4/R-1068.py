import sys
input = sys.stdin.readline
 
n = int(input())

tree = list(map(int, input().split())) 

ac = int(input())

 

def dfs(ac):
    tree[ac] = -100 
    for i in range(n):
        if ac == tree[i]: 
            dfs(i)
dfs(ac)
cnt = 0
for i in range(n):
    if tree[i] != -100 and i not in tree: # 제거된 노드가 아니고 i의 자식이 없다면
        cnt += 1
 
print(cnt)