# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# 그래프를 표현하는 방법은? -> 인접행렬

V = 7
E = 8

adj = [[0] * (V + 1) for _ in range(V + 1)]
edges = list(map(int, input().split()))

for i in range(0, E * 2, 2):
    adj[edges[i]][edges[i + 1]] = 1
    adj[edges[i + 1]][edges[i]] = 1


def bfs(start):
    visited = [0] * (V+1)
    visited[start] = 1

    # 방문할 정점의 목록을 저장하는 queue
    queue = [start]
    while queue:
        # 정점에 방문해서 길 찾기
        # 길 찾으면 방문예정이니까 방문예정목록에 추가
        # 나머지 길 계속 찾기
        front = queue.pop(0)        # BFS의 핵심
        # visited[front] = 1 여기 하는거랑 밑에하는거랑 뭐가 다른지 확인해보기
        print(front, end= ' ')
        # 인접행렬에 나랑 연결된 정점 정보가 있음
        for i in range(1, V+1):
            # i번 노드가 현재 정점과 연결되어있고 방문하지 않았다면
            if adj[front][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1

        print()

bfs(1)