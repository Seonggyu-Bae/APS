import heapq

def primAlgorithm(start):
    my_heap = []
    heapq.heappush(my_heap,(0,start))
    mst = [0] * (V+1)
    weight_sum = 0
    while my_heap:
        weight, vertex = heapq.heappop(my_heap)

        if mst[vertex]:
            continue

        mst[vertex] = 1
        weight_sum += weight
        for linked_idx in range(V+1):
            # 이어지지 않았거나 이미 방문한적이 있으면 pass
            if graph[vertex][linked_idx] == 0 or mst[linked_idx]:
                continue
            heapq.heappush(my_heap,(graph[vertex][linked_idx],linked_idx))

    return weight_sum

T = int(input())

for tc in range(1, T+1):
    V, E = map(int ,input().split())

    graph = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        n1,n2,w = map(int, input().split())

        graph[n1][n2] = w
        graph[n2][n1] = w

    ans = primAlgorithm(0)
    print(f'#{tc} {ans}')