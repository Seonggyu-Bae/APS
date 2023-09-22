di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def solve(a, b, cnt, number):
    if cnt == 6:
        ans.add(number)
        return
    for d in range(4):
        ni, nj = a + di[d], b + dj[d]
        if 0 <= ni < 4 and 0 <= nj < 4:
            number += str(board[ni][nj])
            solve(ni, nj, cnt + 1, number)
            number = number[:-1]


T = int(input())

for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]

    ans = set()

    for i in range(4):
        for j in range(4):
            num = str(board[i][j])
            solve(i, j, 0, num)

    print(f'#{tc} {len(ans)}')
