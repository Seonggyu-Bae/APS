def solve(row, sum_v):
    global min_sum

    if min_sum <= sum_v:    # 백트래킹
        return              # 현재까지 찾은 최솟값보다 지금 계산하는 값이 더 크면 더 볼 필요가 없음

    if row == N:            # N개를 다 골랐으면
        if sum_v < min_sum: # 최솟값이랑 비교해서 작으면 바꿔줌
            min_sum = sum_v
        return

    for col in range(N):
        if not col_check[col]:
            col_check[col] += 1 # 사용중인 열 체크
            solve(row + 1, sum_v + array[row][col])
            col_check[col] -= 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    min_sum = 100       # 최대 10X10 배열에 원소의 최댓값은 10임으로
    array = [list(map(int, input().split())) for _ in range(N)]

    col_check = [0] * N # 한 열에 하나만 골라야 하니까 이걸로 체크를 합니다.

    solve(0, 0)
    print(f'#{tc} {min_sum}')
