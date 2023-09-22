import heapq


# 최단경로 문제 다익스트라를 2번돌리는 문제가 아닐까

def dijkstra(start, end):
    time = [0xfffffff] * (N + 1)
    time[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        pre_time, now = heapq.heappop(heap)

        if time[now] < pre_time:
            continue

        for info in graph[now]:
            next_house = info[0]
            t = info[1]

            new_time = pre_time + t

            if time[next_house] < new_time:
                continue

            time[next_house] = new_time
            heapq.heappush(heap, (new_time, next_house))

    return time[end]


T = int(input())

for tc in range(1, T + 1):
    N, M, X = map(int, input().split())

    # 1 ~ N 번까지의 집 인수의 집은 X

    # x번집에서 y번 집으로 가는데 c시간이 걸리는 단방향 도로 저장
    graph = [[] * (N + 1) for tc in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))

    max_val = 0
    for i in range(1, N+1):
        if i != X:
            temp = dijkstra(i, X) + dijkstra(X, i)
            if temp > max_val:
                max_val = temp
    print(f'#{tc} {max_val}')
