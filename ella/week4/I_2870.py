n = int(input())
arr = []
for i in range(n):
    str = input()
    num = ""
    for j in str:
        if j.isdigit(): # 숫자인 경우
            num += j
        else:
            if num:
                arr.append(int(num)) # '01' -> 1
                num = ""
    if num:
        arr.append(int(num))
arr.sort()
for i in arr:
    print(i)