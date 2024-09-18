n = int(input())
a = list(map(int, input().split()))
stack = [0]
nge = [-1 for _ in range(n)]

for i in range(1, n):
    while stack and a[stack[-1]] < a[i]: # 스택이 비어있지 X && 스택의 최상단 값의 arr 값이 arr[i] 값보다 작을 경우
        nge[stack.pop()] = a[i]
    stack.append(i)

print(*nge)