'''
지렁이: 현재 위치 포함 인접한 1칸까지 배추 보호

'''
T = int(input())
answer = []
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        y, x = map(int, input().split())
        field[y][x] = 1
    
    