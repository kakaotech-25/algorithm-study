ls = list(input())
ls.sort()
dict = {}
for i in ls:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
cnt = 0
center = ''
for key, value in dict.items():
    if value % 2 == 1:
        cnt += 1
        center = key
    if cnt > 1:
        print("I'm Sorry Hansoo")
        exit(0)
ans = ''
for word, times in dict.items():
    ans += (word*(times//2))
print(ans+center+ans[::-1])