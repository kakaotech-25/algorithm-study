## 자꾸 30프로에서 틀려요. 해결한분 삐삐 쳐주세요.


import sys

input = sys.stdin.readline

p, c = map(int, input().split())

if (p <=c) or p/2 > c: 
    print("NO")
else:
    print(p-c)
    print("YES")
    while(True):
        if(p==(c+1)):
            num = (p+c-1)//2
            print('a'+'ba'*num)
            break
        p -=2
        c-=1
        print('aba')