def my_dfs2(v, adj_matrix, visited):
    visited[v] = 1

    for i in range(1, V + 1):
        if adj_matrix[v][i] and not visited[i]:
            my_dfs2(i, adj_matrix, visited)


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        s, e = map(int, input().split())
        adj_matrix[s][e] = 1

    # 경로의 존재를 확인할 출발 노드 S와 도착 노드 G
    S, G = map(int, input().split())

    # DFS의 시작점을 S로 두고 돌린다
    my_dfs2(S, adj_matrix, visited)

    # 다 돌리고 visited[G] 가 0이면 갈 수 없는 것이고 갈 수있으면 1이라고 나올것이다.
    print(f'#{tc} {visited[G]}')
