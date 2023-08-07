T = int(input())
# my_arr = [list(map(int, input().split())) for _ in range(N)]
for tc in range(1, T + 1):
    red = [[0] * 10 for _ in range(10)]
    blue = [[0] * 10 for _ in range(10)]
    purple = 0
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    max_i = 0
    min_i = 10
    max_j = 0
    min_j = 10
    for i in range(N):
        r1 = info[i][0]
        r2 = info[i][2]
        c1 = info[i][1]
        c2 = info[i][3]
        max_r = r1 if r1 > r2 else r2
        min_r = r1 if r1 < r2 else r2
        max_c = c1 if c1 > c2 else c2
        min_c = c1 if c1 < c2 else c2

        if max_i < max_r:
            max_i = max_r
        if min_i > min_r:
            min_i = min_r
        if max_j < max_c:
            max_j = max_c
        if min_j > min_c:
            min_j = min_c

        if info[i][4] == 1:
            for red_i in range(min_r, max_r + 1):
                for red_j in range(min_c, max_c + 1):
                    red[red_i][red_j] += red[red_i][red_j] + 1
        else:
            for blue_i in range(min_r, max_r + 1):
                for blue_j in range(min_c, max_c + 1):
                    blue[blue_i][blue_j] += blue[blue_i][blue_j] + 1

    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if red[i][j] != 0 and blue[i][j] != 0:
                purple += 1

    print(f'#{tc} {purple}')
