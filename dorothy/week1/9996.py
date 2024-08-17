'''
regex
1: N (1<=N<=100)
2: 패턴 (a-z, *) (length<=100) *는 시작과 끝 x
3~: N줄 (a-z) (length<=100)
'''
import re

N = int(input())
pattern = input()
strings = [input() for _ in range(N)]

pattern = ".*".join(pattern.split("*"))
p = re.compile(pattern)

for s in strings:
    if p.fullmatch(s):
        print("DA")
    else:
        print("NE")
