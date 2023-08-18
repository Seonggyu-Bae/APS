def BFS(G, v):                      # 그래프: G, 탐색 시작점: v
    visited = [0] * (n+1)           # n : 정점의 개수
    queue = []                      # 큐 생성
    queue.append(v)                 # 시작점 v를 큐에 삽입
    while queue:                    # 큐가 비어있지 않은 경우
        t = queue.pop(0)            # 큐의 첫번째 원소 반환
        if not visited[t]:          # 방문되지 않은 곳이라면
            visited[t] = True       # 방문 표시
            visit(t)                # 정점 t에서 할 일
            for i in G[t]:          # t 와 연결된 모든 정점에 대해
                if not visited[i]:  # 방문되지 않은 곳이라면
                    queue.append(i) # 큐에 넣기