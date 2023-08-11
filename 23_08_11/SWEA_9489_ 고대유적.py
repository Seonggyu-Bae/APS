T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    photo_data = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0

    for i in range(N):
        col_count = 0

        for j in range(M):
            if photo_data[i][j] == 1:
                col_count += 1
                if col_count > max_count:
                    max_count = col_count
            else:
                col_count = 0

    for i in range(M):
        row_count = 0
        for j in range(N):
            if photo_data[j][i] == 1:
                row_count += 1
                if row_count > max_count:
                    max_count = row_count
            else:
                row_count = 0

    print(f'#{tc} {max_count}')
