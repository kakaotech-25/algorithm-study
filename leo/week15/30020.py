import sys
input = sys.stdin.readline

A, B = map(int, input().split())

minValue = min(A, B)

#재료 준비
patty = A
cheese = B

# 버거 제작
def make_bugger(*, patty, cheese):
    # 햄버거의 개수 = 두 재료의 개수 차이
    total_bugger_count = patty - cheese
    print(total_bugger_count)

    # 한개만 빼고 전부 더블패티 치즈버거
    for _ in range(total_bugger_count - 1):
        patty -= 2
        cheese -= 1
        print('aba')

    # 스택 치즈버거
    loop = True
    while(loop):
        # 패티넣고
        if (patty):
            print('a', end="")
            patty -= 1
        # 패티 다 쓰면 끝
        else:
            print('')
            return
        # 치즈 넣고
        if (cheese):
            print('b', end="")
            cheese -= 1

# 만들수있는 조건:
# 1. 패티의 개수가 치즈 개수 두배 이상 차이나면 모두 사용할 수 없음.
# 2. 치즈가 더 많거나 
if patty > (cheese * 2) or cheese > patty:
    print("NO")
else:
    print("YES")
    make_bugger(patty=patty, cheese=cheese)


