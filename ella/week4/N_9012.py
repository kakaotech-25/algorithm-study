t = int(input())
for i in range(t):
    str = input()
    stack = []
    for j in str:
        if len(stack) == 0:
            stack.append(j)
        elif j == ")" and j != stack[-1]:
            stack.pop()
        else:
            stack.append(j)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")