'''
문자열을 영어 알파벳을 13글자씩 밀어서 만든다.

1: 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S(1<=S<=100)

출력: 암호화한 내용
'''
S = input()
ans = ""

for c in S:
    if c.isupper():
        location = (ord(c)+13-ord('A'))%26
        ans += chr(location + ord('A'))
    elif c.islower():
        location = (ord(c)+13-ord('a'))%26
        ans += chr(location + ord('a'))
    else:
        ans += c

print(ans)