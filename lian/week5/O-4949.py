while True:
    flag = 1
    tmp = []
    ls = list(input())
    if len(ls) == 1 and ls[0] == '.':
        break

    for i in range(len(ls)):
        if ls[i] == '(' or ls[i] == '[':
            tmp.append(ls[i])
        elif ls[i] == ')':
            if len(tmp) != 0 and tmp[-1] == '(':
                tmp.pop()
            else:
                flag = 0
        elif ls[i] == ']':
            if len(tmp) != 0 and tmp[-1] == '[':
                tmp.pop()
            else:
                flag = 0
    if flag == 1 and len(tmp) == 0:
        print('yes')
    else:
        print('no')