def re(i, j, N, val):
    global min_sum
    if i >= N or j >= N:
        return
    if (i, j) == (N - 1, N - 1):
        if min_sum > val+board[i][j]:
            min_sum = val+board[i][j]
        return
    else:
        re(i, j + 1, N, val + board[i][j])
        re(i + 1, j, N, val + board[i][j])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 2000
    i, j = 0, 0

    re(i, j, N, 0)
    print(f'#{tc} {min_sum}')
