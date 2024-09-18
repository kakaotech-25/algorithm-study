N = int(input())
tree = list(map(int, input().split()))
node = int(input())
ans = 0

def dfs(tmp):
    tree[tmp] = -2
    for i in range(N):
        if tree[i] == tmp:
            dfs(i)

dfs(node)
for i in range(N):
    if tree[i] != -2:
        if i not in tree:
            ans += 1
print(ans)