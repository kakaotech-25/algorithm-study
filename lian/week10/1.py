# N명의 적
# H만큼의 체력
# i번째 발사로 적을 맞추면 ((i-1) mod 4) + 1 만큼의 체력이 깎이게 됨 ((i-1)/4)+1
# 체력 0 이하면 쓰러짐
# ans = 권총을 발사해야 하는 횟수

N = int(input())
H = list(map(float, input().split()))
ans = 0
while H:
	ans += 1
	H[0] -= (((ans-1)%4)+1)
	if H[0] <= 0:
		H.pop(0)
print(ans)