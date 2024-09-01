n = int(input())
team1 = 0
team2 = 0
cnt = 0 # 우승팀 확인 count(양수일 경우 team1이, 음수일 경우 team2가 이기고 있음)

for i in range(n):
    team, time = input().split(" ")
    min, sec = map(int, time.split(":"))
    if team == "1":
        if cnt == 0: # team1이 이기고 있는 경우
            team1 += 48*60 - (60*min+sec)
        cnt += 1
        if cnt == 0: # team1이 지다가 동점이 된 경우
            if team2 != 0:
                team2 -= 48*60 - (60*min+sec) #team2가 이기고 있는 시간 종료
    if team == "2":
        if cnt == 0:
            team2 += 48*60 - (60*min+sec)
        cnt -= 1
        if cnt == 0: 
            if team1 != 0:
                team1 -= 48*60 - (60*min+sec)

print(f"{team1//60:02d}:{team1%60:02d}")
print(f"{team2//60:02d}:{team2%60:02d}")
