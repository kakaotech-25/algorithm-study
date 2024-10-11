import sys

input = sys.stdin.readline

n= int(input())

def de(n):
    if n==1:
        return['*']
    stars = de(n//3)
    re =[]
    
    for i in stars:
        re.append(i*3)
    for i in stars:
        re.append(i+' '*(n//3)+i)
    for i in stars:
        re.append(i*3)
    
    return re

print('\n'.join(de(n)))