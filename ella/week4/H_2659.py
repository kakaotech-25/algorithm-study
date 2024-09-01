vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    str = input()
    y_cnt = 0
    n_cnt = 0
    back = ""
    answer = False

    if str == 'end':
        break

    for i in str:
        if i in vowel:
            answer = True
            y_cnt += 1
            n_cnt = 0
            if y_cnt >= 3:
                answer = False
                break
        else:
            n_cnt += 1
            y_cnt = 0
            if n_cnt >= 3:
                answer = False
                break
        if i == back and i not in ('e', 'o'):
            answer = False
            break

        back=i

    if answer == True:
        print(f"<{str}> is acceptable.")
    else:
        print(f"<{str}> is not acceptable.")
