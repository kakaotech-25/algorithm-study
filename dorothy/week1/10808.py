'''
1<=len(S)<=100
단어에 포함된 a~z의 개수를 공백으로 구분해 출력
'''
S = input()
ans = ''
for i in range(26):
    cnt = S.count(chr(ord('a')+i))
    ans += f"{cnt} "

print(ans)