def re(i, j, N, val):
    if (i, j) == (N - 1, N - 1):
        ans.append(val)
        return
    else:
        for d in range(2):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                re(ni, nj, N, val + board[ni][nj])


di = [1, 0]
dj = [0, 1]
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    i, j = 0, 0
    val = board[0][0]

    re(i, j, N, val)
    print(f'#{tc} {min(ans)}')
