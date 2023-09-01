di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    max_v = N ** 2 + 1

    i, j = 0, 0

    for p in range(N):
        for q in range(N):
            i, j = p, q
            cnt = 1
            start = room[i][j]

            while True:
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < N and 0 <= nj < N and room[ni][nj] == room[i][j] + 1:
                        cnt += 1
                        i, j = ni, nj
                        break
                else:
                    break
            if cnt > max_cnt:
                max_cnt = cnt
                max_v = start
            elif cnt == max_cnt and start < max_v:
                max_v = start

    print(f'#{tc} {max_v} {max_cnt}')
