vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    pw = input()
    if pw == 'end':
        break
    else:
        check = True

        # 모음이 하나도 없는 경우
        vcnt = 0
        for i in pw:
            if i in vowel:
                vcnt += 1
        if not vcnt:
            check = False

        #모음이나 자음이 3개 연속으로 오는 경우
        if len(pw) >= 3:
            for i in range(len(pw)-2):
                if pw[i] in vowel and pw[i+1] in vowel and pw[i+2] in vowel:
                    check = False
                elif pw[i] not in vowel and pw[i+1] not in vowel and pw[i+2] not in vowel:
                    check = False

        # 같은 글자 연속 두번인 경우 (e, o는 허용)
        if len(pw) >= 2:
            for i in range(len(pw)-1):
                if pw[i] == pw[i+1] and pw[i] != 'e' and pw[i] != 'o':
                    check = False

    #결과 출력
    if check:
        print(f'<{pw}> is acceptable.')
    else:
        print(f'<{pw}> is not acceptable.')