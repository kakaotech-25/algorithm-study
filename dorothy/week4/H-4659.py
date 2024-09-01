'''
re.match("[aeiou]", pw) O
[aeiou]{3} X
[b-dfj-np-tv-z]{3} X
[a-df-np-z]{2} X
'''
import re

pw = None
pws = []
while pw != "end":
    pw = input()
    pws.append(pw)
pws.pop()

for p in pws:
    first = re.search(r"[aeiou]+", p)
    second1 = re.match(r"[aeiou]{3}", p)
    second2 = re.match(r"[b-dfj-np-tv-z]{3}", p)
    third = [chr(ord('a') + i) * 2 for i in range(26)]
    #print(first)
    #print(second1)
    #print(second2)
    #print(third)

    if first and not (second1 or second2):
        acceptable = True
        for substr in third:
            if substr == "ee" or substr == "oo":
                continue
            if substr in p:
                acceptable = False
                print(f"<{p}> is not acceptable.")
                break
        if acceptable:
            print(f"<{p}> is acceptable.")
    else:
        print(f"<{p}> is not acceptable.")