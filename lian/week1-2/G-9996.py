N = int(input())
start, end = input().split("*")
check_len = len(start) + len(end)
for _ in range(N):
    tmp = input()
    if check_len <= len(tmp) and tmp.startswith(start) and tmp.endswith(end):
        print("DA")
    else:
        print("NE")
