# 첫글자가 같은 선수 5명 선발
# 5명보다 적다면 기권
# 첫줄에 선수의 수, 그다음에 순서대로 선수의 성
# 선발할 수 있는 경우에는 가능한 성의 첫글자를 사전순으로 공백없이 출력
# ord('a) = 97
n = int(input())

mem = [0]*n
asci = [0]*26

for i in range(n):
    mem[i] = input()
    asci[ord(mem[i][0])-97] +=1
re=''
for i in range(26):
    if asci[i]>4:
        re+=chr(i+97)

if re=='':
    print('PREDAJA')
else:
    print(re)