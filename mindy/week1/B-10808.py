str = input()


for i in range(26):
    cnt=str.count(chr(i+97))
    print(cnt,end=' ')

