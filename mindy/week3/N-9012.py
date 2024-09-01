from collections import Counter

n = int(input())

for _ in range(n):
    stack =[]
    s = input()
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
    