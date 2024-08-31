n = int(input())
ans = []
for i in range(n):
    tmp = input()
    num = ''
    for i in tmp:
        if i.isdigit():
            num += i
        else:
            if num:
                ans.append(int(num))
                num = ''
    if num:
        ans.append(int(num))
ans.sort()
for i in ans:
    print(i)