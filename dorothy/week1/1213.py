'''
palindrome
1:알파벳 대문자 최대 50글자, 조합해서 팰린드롬 만들어주기.
'''
def palindrome(s):
    d = {}

    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    odd = ''
    p = ''
    for idx, val in dict(sorted(d.items())).items():
        p += idx * (val // 2)
        if val % 2 == 1:
            if not odd:
                odd = idx
            else:
                return "I'm Sorry Hansoo"
    
    return "".join([p, odd]) + "".join(reversed(p))

s = input()
print(palindrome(s))
