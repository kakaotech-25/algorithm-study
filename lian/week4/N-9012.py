n = int(input())
for i in range(n):
    ls = list(input())
    ans = []
    check = 0
    for i in range(len(ls)):
        if len(ans) == 0 and ls[i] == ')':
            check = 1
            break
        elif ls[i] == '(':
            ans.append(ls[i])
        elif ls[i] == ')':
            ans.pop()
    if len(ans) == 0:
        if check == 1:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')