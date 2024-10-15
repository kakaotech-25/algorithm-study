import sys

input=sys.stdin.readline

from itertools import combinations

while(True):
    
    knum = list(map(int,input().split()))
    k = knum[0]
    if(k ==0): break
    knum.pop(0)
    

    
   # knum.sort()
    kre = combinations(knum, 6)
    
    for i in kre:
        print(*i)
    print()