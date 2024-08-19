ls = list(input())
ans = ''
# a = 97 / A = 65 로 계산한다.

for i in ls:
    if i.islower():
        tmp = chr((ord(i) + 13 - 97) % 26 + 97)
    elif i.isupper():
        tmp = chr((ord(i) + 13 - 65) % 26 + 65)
    else:
        tmp = i
    ans += tmp
print(ans)