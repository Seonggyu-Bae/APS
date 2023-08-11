T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flower_data = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(N):
        for j in range(M):
            count = 0
            count += flower_data[i][j]
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    count += flower_data[nx][ny]
            if count > max_count:
                max_count = count

    print(f'#{tc} {max_count}')