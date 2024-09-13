while True:
    str = input()
    if str == ".":
        break
    stack = []
    for i in str:
        if i == "(" or i == "[": 
            stack.append(i)
        if i == ")":
            if len(stack) != 0 and "(" == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
                break
        if i == "]":
            if len(stack) != 0 and "[" == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")