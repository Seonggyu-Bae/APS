import heapq

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def dijkstra():
    time = [[0xffffffff] * N for _ in range(N)]
    time[0][0] = 0
    heap = []
    heapq.heappush(heap, (0, 0, 0))

    while heap:
        pre_sum_time, i, j = heapq.heappop(heap)

        if time[i][j] < pre_sum_time:
            continue

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:

                new_sum_time = pre_sum_time + info[ni][nj]

                if time[ni][nj] <= new_sum_time:
                    continue

                time[ni][nj] = new_sum_time
                heapq.heappush(heap, (new_sum_time, ni, nj))

    return time[N-1][N-1]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    info = [list(map(int, input())) for _ in range(N)]
    ans = dijkstra()
    print(f'#{tc} {ans}')
