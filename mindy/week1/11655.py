# 알파벳을 13글자씩 밀기
# 알파벳이 아닌 글지는 그대로 남아있기

# 아스키 코드 a = 97, A = 65

# ord, chr

s= input()
re=''

for i in s:
    if ord(i)>96 and ord(i)<123:
        if ord(i)+13>122:
            i = chr(ord(i)-13)
        else: i = chr(ord(i)+13)
        re+=i
    elif ord(i)>64 and ord(i)<91:
        if ord(i)+13>90:
            i = chr(ord(i)-13)
        else: i = chr(ord(i)+13)
        re+=i
    else: re+=i

print(re)