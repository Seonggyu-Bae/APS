T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    my_arr = [list(map(int,input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_sum = 0

    for i in range(N):
        for j in range(M):
            temp_sum = my_arr[i][j]
            for k in range(4):
                for t in range(1, my_arr[i][j]+1):
                    ni, nj = i + di[k]*t, j + dj[k]*t
                    if 0 <= ni < N and 0 <= nj < M:
                        temp_sum += my_arr[ni][nj]
            if temp_sum > max_sum:
                max_sum = temp_sum

    print(f'#{tc} {max_sum}')
