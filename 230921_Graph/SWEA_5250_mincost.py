di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

import heapq


def Dijkstra(si, sj):
    distance = [[0xfffffff] * (N + 1) for _ in range(N + 1)]

    distance[si][sj] = 0

    priorityQ = []

    heapq.heappush(priorityQ, (0, si, sj))

    while priorityQ:

        pre_cost, i, j = heapq.heappop(priorityQ)

        if distance[i][j] < pre_cost:
            continue

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                h = height[ni][nj]

                if h > height[i][j]:
                    new_cost = pre_cost + h - height[i][j] + 1
                else:
                    new_cost = pre_cost + 1

                if distance[ni][nj] <= new_cost:
                    continue

                distance[ni][nj] = new_cost
                heapq.heappush(priorityQ, (new_cost, ni, nj))

    return distance[N - 1][N - 1]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]

    ans = Dijkstra(0, 0)
    print(f'#{tc} {ans}')
