def loop(p, e):
    global node_count

    is_f = 0
    si_count = len(edges[p])

    for i in range(1, si_count):
        if edges[p][i] != 0:
            node_count += 1
            is_f = 1
            loop(edges[p][i], e)

    if is_f == 0:
        return 0


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())

    edges = [[0] for _ in range(E + 2)]

    edge_info = list(map(int, input().split()))
    node_count = 1
    for i in range(0, len(edge_info), 2):
        edges[edge_info[i]].append(edge_info[i + 1])

    loop(N, E)

    print(f'#{tc} {node_count}')
