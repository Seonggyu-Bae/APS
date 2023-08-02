T = int(input())
for tc in range(1, T + 1):
    count = 0
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    # 행 탐색
    for i in range(N):
        temp = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                temp += 1
                # 길이가 K인 공간을 발견
                if temp == K:
                    # j에 따라서 count할지말지 결정함
                    # N-1보다 작으면 그 다음이 막혀있어야 count 올림
                    if j < N - 1:
                        if puzzle[i][j + 1] == 0:
                            count += 1
                    # N-1이면 그 다음이 없으니까 count 올림
                    if j == N - 1:
                        count += 1

            else:
                temp = 0

    # 열 탐색
    for i in range(N):
        temp = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                temp += 1
                if temp == K:
                    if j < N - 1:
                        if puzzle[j + 1][i] == 0:
                            count += 1
                    if j == N - 1:
                        count += 1
            else:
                temp = 0

    print(f'#{tc} {count}')
