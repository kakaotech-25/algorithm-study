# 가운데를 기준으로 나눠서 


s = input()
start = len(s)//2
if len(s)%2 ==0:
    pre = s[:start]
    suf= s[start:]
    suf = suf[::-1]
    if pre == suf:
        print(1)
    else:
        print(0)
else:
    pre = s[:start]
    suf= s[start+1:]
    suf = suf[::-1]
    if pre == suf:
        print(1)
    else:
        print(0)