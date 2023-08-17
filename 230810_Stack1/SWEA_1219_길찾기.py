def dfs1(start, adj1, adj2, visited):
    stack = [start]
    visited[start] = 1

    while stack:
        top = stack[-1]
        visited[top] = 1
        if top == 99:
            return 1

        for i in range(200):
            if adj1[top] != 0 and not visited[adj1[top]]:
                stack.append(adj1[top])
                break
            elif adj2[top] != 0 and not visited[adj2[top]]:
                stack.append(adj2[top])
                break
        else:
            stack.pop()


for _ in range(10):
    tc, line = map(int, input().split())

    visited = [0] * 100

    adj_matrix1 = [0] * 100
    adj_matrix2 = [0] * 100
    edge_info = list(map(int, input().split()))

    for i in range(0, line * 2, 4):
        adj_matrix1[edge_info[i]] = edge_info[i + 1]

    for i in range(2, line * 2, 4):
        adj_matrix2[edge_info[i]] = edge_info[i + 1]

    dfs1(0, adj_matrix1, adj_matrix2, visited)
    print(f'#{tc} {visited[99]}')
