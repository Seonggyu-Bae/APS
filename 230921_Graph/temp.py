import heapq


def primalgo(start):
    heap = []
    heapq.heappush(heap, (0, start))
    mst = [0] * N
    weight = [0xfffffff] * N
    weight[start] = 0
    while heap:
        L, vertex = heapq.heappop(heap)

        if mst[vertex]:
            continue
        mst[vertex] = L
        for i in range(N):
            if mst[i] or i == vertex:
                continue

            heapq.heappush(heap, (min_val, i))

    temp = 0
    for i in range(1, N):
        temp += mst[i]

    return temp * E


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    island = [list(map(int, input().split())) for _ in range(2)]
    E = float(input())

    distance = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 환경부담금 계산에 거리의 제곱을 써서 sqrt 는 생략함
            distance[i][j] = abs(island[0][i] - island[0][j]) ** 2 + abs(island[1][i] - island[1][j]) ** 2

    ans = primalgo(0)

    if ans - int(ans) >= 0.5:
        ans = int(ans) + 1
    else:
        ans = int(ans)
    print(f'#{tc} {ans}')
