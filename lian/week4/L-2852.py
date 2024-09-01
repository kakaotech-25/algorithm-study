n = int(input())
score = {1:0, 2:0}
ans = {1:0, 2:0}
winning = 0 #이기고 있었던 팀을 저장, 0=비김
prev = 0 #이전 점수 부여했던 시간 저장
for _ in range(n):
    ls = list(map(str, input().split()))
    team = int(ls[0])
    m, s = ls[1].split(':')
    time = int(m) * 60 + int(s)
    score[team] += 1 #이긴 팀에 점수 +1
    if winning == 0: #이전까지 비기고 있었음
        prev = time
        winning = team
    elif winning and score[1] == score[2]: # # 이전에 이기고 있던 팀이 있었는데 이제 비김
        ans[winning] += (time - prev) #이기고 있던 팀에게 이제까지의 시간을 더해줌
        prev = time
        winning = 0 #비김상태로 바꿔줌

if winning: #게임이 종료될때까지 이기고 있는 팀이 있었을 때
    ans[winning] += (48*60) - prev

print("%02d:%02d" %(ans[1]//60, ans[1]%60))
print("%02d:%02d" %(ans[2]//60, ans[2]%60))


