di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def solve(i, j, N):
    global cnt
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and room[ni][nj] == room[i][j] + 1:
            cnt += 1
            solve(ni, nj, N)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    max_v = N ** 2 + 1

    for i in range(N):
        for j in range(N):
            cnt = 1
            solve(i, j, N)
            if cnt > max_cnt:
                max_cnt = cnt
                max_v = room[i][j]
            if cnt == max_cnt and room[i][j] < max_v:
                max_cnt = cnt
                max_v = room[i][j]

    print(f'#{tc}', max_v, max_cnt)
