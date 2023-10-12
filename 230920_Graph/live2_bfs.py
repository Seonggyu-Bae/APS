graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]


def bfs(start):
    visited = [0] * len(graph)

    # 먼저 방문 했던 것을 먼저 처리해야한다. = queue

    Q = [start]
    visited[start] = 1

    while Q:
        # queue의 맨 앞 요소를 꺼냄
        now = Q.pop(0)
        print(now, end=' ')

        # 인접한 노드들을 queue에 추가
        for next_vertex in range(len(graph)):
            # 연결이 안되어 있다면 continue
            if graph[now][next_vertex] == 0:
                continue

            # 방문한 지점이라면 queue에 추가하지 않음
            if visited[next_vertex]:
                continue

            Q.append(next_vertex)
            # BFS 이므로 여기서 방문 체크를 해주어도 상관없다.
            visited[next_vertex] = 1


bfs(0)
