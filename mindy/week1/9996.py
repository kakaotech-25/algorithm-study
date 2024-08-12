# ab*cde 인 경우도 고려하기
# a*a인 경우 a를 넣으면 틀림!

n = int(input())
pat = input().split("*")
length = len(pat[0])+len(pat[1])
for i in range(n):
    str = input()
    if length <= len(str):
        if str.startswith(pat[0]) and str.endswith(pat[1]):
            print('DA')
        else: print('NE')

    else: print('NE')
