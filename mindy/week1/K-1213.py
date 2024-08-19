"""counter로 갯수 세고 홀수인것을 가운데로
mid를 선언해주지 않고 그냥 사용했다가... 계속 런타임 에러(NameError)가 발생했음 ㅜㅜ
앞으로 주의하기!"""
import sys
from collections import Counter

input = sys.stdin.readline

n = input().strip()
re=''
mid=''
n_word = Counter(n)
cnt = 0
for k,v in list(n_word.items()):
    if v % 2 == 1:
        mid = k
        cnt +=1
        if cnt >=2:
            print("I'm Sorry Hansoo")
            sys.exit(0)

for k,v in sorted(n_word.items()):
    re +=(k*(v//2))
# 문자의 빈도를 절반으로 줄임
print(re+mid+re[::-1])