di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]
N, M, K = map(int, input().split())

# fire_ball[0],[1] : 파이어볼 좌표(r,c)
# fire_ball[2] : 파이어볼 질량
# fire_ball[3] : 파이어볼 속력
# fire_ball[4] : 파이어볼 방향 (0~7) 시계방향 0 = 상
fire_ball = [list(map(int, input().split())) for _ in range(M)]


