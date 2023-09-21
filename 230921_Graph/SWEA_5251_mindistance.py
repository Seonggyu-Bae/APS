import heapq


def Dijkstra(start):
    distance = [0xfffffff] * (N + 1)
    distance[start] = 0
    priorityQ = []
    heapq.heappush(priorityQ, (0, start))

    while priorityQ:
        pre_dis, now = heapq.heappop(priorityQ)

        if distance[now] < pre_dis:
            continue

        for info in graph[now]:
            next_node = info[0]
            cost = info[1]

            new_cost = pre_dis + cost

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(priorityQ, (new_cost, next_node))

    return distance[N]


T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])

    ans = Dijkstra(0)

    print(f'#{tc} {ans}')