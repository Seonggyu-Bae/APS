T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    x, y, dir_v, num = 0, 0, 0, 1
    snail = [[0] * N for _ in range(N)]

    while num <= N ** 2:
        snail[x][y] = num

        ndx, ndy = x + di[dir_v], y + dj[dir_v]

        if ndx < 0 or ndx >= N or ndy < 0 or ndy >= N or snail[ndx][ndy] != 0:
            dir_v = (dir_v + 1) % 4

        x += di[dir_v]
        y += dj[dir_v]
        num += 1

    print(f"#{test_case}")
    for s in snail: print(*s)