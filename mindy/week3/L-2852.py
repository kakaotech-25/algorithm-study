n = int(input())

first =0
second = 0
flag =0
for i in range(n):
    team, time = input().split()
    
    m,s = map(int, time.split(':'))
    
    if team == '1':
        if flag ==0:
            first +=48*60-(60*m+s)
        flag+=1
        if flag == 0:
            if second>0:
                second = second-(48*60-(60*m+s))
    else:
        if flag ==0:
            second +=48*60-(60*m+s)
        flag-=1
        if flag == 0:
            if first>0:
                first = first-(48*60-(60*m+s))

print('{:0>2}:{:0>2}'.format(first//60,first%60))
print('{:0>2}:{:0>2}'.format(second//60,second%60))