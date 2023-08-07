T = int(input())
# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

# 대각 우상 우하 좌상 좌하
di1 = [-1, 1, -1, 1]
dj1 = [1, 1, -1, - 1]


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0
    for i in range(N):
        for j in range(N):
            # tempkill1 : 상하좌우 tempkill2 : 대각
            temp_kill1 = info[i][j]
            temp_kill2 = info[i][j]
            for l in range(1, M):
                for k in range(0,4):
                    ndi, ndj, ndi1, ndj1 = i + di[k] * l, j + dj[k] * l, i + di1[k] * l, j + dj1[k] * l
                    if 0 <= ndi < N and 0 <= ndj < N:
                        temp_kill1 += info[ndi][ndj]
                    if 0 <= ndi1 < N and 0 <= ndj1 < N:
                        temp_kill2 += info[ndi1][ndj1]
            if temp_kill1 > max_kill:
                max_kill = temp_kill1
            if temp_kill2 > max_kill:
                max_kill = temp_kill2

    print(f'#{tc} {max_kill}')
