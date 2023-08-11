def myDFS(start, end, adj):
    visited = [0] * (len(adj))
    visited[start] = 1
    top = 0
    d_stack = [start]

    while d_stack:
        for i in range(1, len(adj)):
            if adj[d_stack[top]][i] and not visited[i]:
                d_stack.append(i)
                visited[i] = 1
                top += 1
                break
        else:
            d_stack.pop(top)
            top -= 1

    return visited[end]


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())
        adj[start][end] = 1

    S, G = map(int, input().split())

    print(f'#{tc} {myDFS(S, G, adj)}')
