import sys
input = sys.stdin.readline

n = int(input())
narr = set(map(int,input().split()))

m = int(input())
marr = list(map(int,input().split()))
re =[]
for i in marr:
    if i in narr:
        re.append("1")
    else:
        re.append("0") 
        
        
print(' '.join(re))