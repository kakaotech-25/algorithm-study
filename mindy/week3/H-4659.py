# 1.모음 하나를 반드시 포함해야함
# 2.모음이 3개 혹은 자음이 3개 연속으로 오면 안된다
# 3.같은 글자가 연속적으로 두번 오면 안되나, ee와 oo는 허용한다. 


import re

vowels = "[aeiouAEIOU]"
consonants = "[^aeiouAEIOU\s\d]"

while(True):
    word = input()
    if word == 'end':
        break
    pattern1 = f"({vowels}{{3,}}|{consonants}{{3,}})"
    pattern2 = r"(.)\1"
    exceptions = ["ee", "oo"]
    
    has_vowel = re.search(vowels, word) is not None
    
    if not has_vowel:
        print("<"+word+"> is not acceptable.")
    elif re.search(pattern1,word):
        print("<"+word+"> is not acceptable.")
    elif re.search(pattern2,word) and not any(exc in word for exc in exceptions):
        print("<"+word+"> is not acceptable.")
    else : 
        print("<"+word+"> is acceptable.")