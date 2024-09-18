n = int(input())
arr = list(map(int, input().split()))
node = int(input())

def dfs(num):
    arr[num] = -2 # 노드 제거(-2)
    for i in range(n):
        if num == arr[i]:
            dfs(i)

dfs(node)
cnt = 0
for i in range(n):
    if arr[i] != -2 and i not in arr: # 노드 삭제 X && i의 자식 노드가 없을 경우
        cnt += 1
print(cnt)