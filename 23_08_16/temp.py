def solve(row,sum_v):
    global min_sum

    if min_sum <= sum_v:
        return

    if row == N:
        if sum_v < min_sum:
            min_sum = sum_v
        return

    for col in range(N):
        if not col_check[col]:
            col_check[col] += 1
            solve(row + 1, sum_v + array[row][col])
            col_check[col] -= 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    min_sum = 100
    array = [list(map(int, input().split())) for _ in range(N)]
    col_check = [0] * N
    solve(0,0)
    print(f'#{tc} {min_sum}')