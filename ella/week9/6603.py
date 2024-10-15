import sys
input = sys.stdin.readline

def back(a1, a2):
    if len(a2) == 6:
        print(" ".join(map(str, a2)))
        return
    else:
        for i in a1:
            if len(a2) == 0 or i > a2[-1]:
                a2.append(i)
                back(a1, a2)
                a2.pop()

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        break
    s = arr[1:]
    answer = []

    back(s, answer)
    print()