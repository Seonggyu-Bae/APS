def bfs(s, V):  # 시작정점 s, 마지막 정점번호 V
    visited = [0] * (V + 1)  # visited 생성
    Q = []  # 큐 생성
    Q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문 표시

    while Q:  # 큐에 정점이 남아있으면 (front != rear)
        t = Q.pop(0)  # dequeue
        print(t)  # 방문한 정점에서 할 일을 쓰면됨
        for w in adj_l[t]:
            if visited[w] == 0:  # 인접한 정점 중 인큐되지 않은 정점이 있으면
                Q.append(w)  # enqueue
                visited[w] = visited[t] + 1  # enqueue 표시(visited) 이렇게 하면 거리를 사용가능


"""
7 8 
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

V, E = map(int, input().split())  # 1번부터 V개의 정점, E개의 간선
arr = list(map(int, input().split()))

# 인접리스트
adj_l = [[] for _ in range(V + 1)]

for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

print(adj_l)

bfs(1, 7)
