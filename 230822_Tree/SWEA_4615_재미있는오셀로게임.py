di = [1, -1, 0, 0, -1, 1, -1, 1]
dj = [0, 0, 1, -1, 1, 1, -1, -1]


def oselo(i, j, color):
    for d in range(8):          # 상하좌우 대각선
        for k in range(1, N):   # 움직일 수 있는 최대 범위
            ni, nj = i + di[d] * k, j + dj[d] * k
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == color:  # 같은 색을 찾았다면
                    for b in range(1, k):   # i + di[d] *(1~k-1)범위까지 같은 색으로 바꿔주면됨
                        bi, bj = i + di[d] * b, j + dj[d] * b
                        board[bi][bj] = color
                    break                   # 다 바꿔줬으니 다음 방향 보면됨

                elif board[ni][nj] == 0:    # 비어있으면 다음방향 보면됨
                    break

                else:                       # 다른색이라면 일단 계속 탐색함
                    continue
            else:                           # 범위 벗어나면 다음 방향 보면됨
                break
    return 0


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 초기값
    board = [[0] * N for _ in range(N)]
    board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2][N // 2 - 1] = 1

    # -1을 해주는 이유는 입력이 0 ~ N-1이 아니고 1 ~ N까지 들어오기 때문
    for _ in range(M):
        i, j, color = map(int, input().split())
        board[i - 1][j - 1] = color
        oselo(i - 1, j - 1, color)

    # 입력을 모두 처리했으니 보드판 탐색
    black, white = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print(f'#{tc} {black} {white}')
