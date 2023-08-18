def bfs(S, G, V):
    visited = [0] * (V + 1)     # 방문 표시 배열을 만든다
    Q = [S]                     # 큐 처럼 사용할 리스트
    visited[S] = 1              # 시작점 방문표시

    while Q:                    # 큐가 빌 때 까지
        t = Q.pop(0)            # 시작 노드를 큐에서 빼고

        for i in adj_l[t]:      # 시작 노드와 이어진 노드들을 탐색
            if not visited[i]:  # 이어진 노드가 방문하지 않은 노드라면
                Q.append(i)     # 큐에 넣고
                visited[i] = visited[t] + 1 # 방문표시를 하는데 이는 시작노드와의 거리처럼 사용할 것이다.
                if i == G:                  # 이어진 노드가 도착 노드라면
                    return visited[i] - 1   # 거리를 반환함
    return 0                                # 도착 노드에 갈 수 없으면 0을 반환함


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())    # V : 노드의 개수, E : 방향성이 없는 간선

    adj_l = [[] for _ in range(V + 1)]  # 인접 리스트

    for _ in range(E):
        s, e = map(int, input().split())    # 간선의 양쪽 노드 번호
        adj_l[s].append(e)                  # 인접리스트에 표시 해준다 (s노드와 e노드가 이어져있다)
        adj_l[e].append(s)                  # 인접리스트에 표시 해준다 (e노드와 s노드가 이어져있다)

    S, G = map(int, input().split())        # 출발 노드S 도착노드 G

    ans = bfs(S, G, V)
    print(f'#{tc} {ans}')