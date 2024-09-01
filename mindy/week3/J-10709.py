h, w = map(int, input().split())
arr = [input() for _ in range(h)]

for a in arr: 
    lst = [-1 for _ in range(w)]  
    for i in range(w):
        if a[i] == 'c':  
            lst[i] = 0  
    tmp = 0
    for i in range(1, w):
        if lst[i] == 0: 
            tmp = 0
        if lst[i - 1] != -1:  
            if lst[i] != 0:  
                tmp += 1
                lst[i] = tmp
    print(*lst)
