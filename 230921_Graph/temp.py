import heapq

def primalgo(start):
    heap = []
    heapq.heappush(heap, (1, start))
    mst = [0] * N
    while heap:
        L, vertex = heapq.heappop(heap)

        if mst[vertex]:
            continue
        mst[vertex] = L
        for i in range(N):
            if mst[i] or i == vertex:
                continue
            heapq.heappush(heap, (L + distance[vertex][i], i))
    return mst


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

    a = primalgo(0)
    print(a[len(a)-1] * E)
    # ans = 0
    # for i in range(1, len(a)):
    #     ans += a[i]
    # ans *= E
    #
    # if ans - int(ans) >= 0.5:
    #     ans = int(ans) + 1
    # else:
    #     ans = int(ans)
    # print(f'#{tc} {ans}')
