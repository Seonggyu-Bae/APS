def bfs(s, V):  # 시작정점 s, 마지막 정점번호 V
    visited = [0] * (V + 1)  # visited 생성
    Q = [None] * 100  # 큐 생성
    front = rear = -1
    rear += 1
    Q[rear] = 1  # 시작점 enqueue
    visited[s] = 1  # 시작점 방문 표시

    while rear != front:  # 큐에 정점이 남아있으면 (front != rear)
        front += 1
        t = Q[front]  # 경로 탐색할 정점을 큐에서 dequeue
        print(t)  # 방문한 정점에서 할 일을 쓰면됨
        for w in range(1, V+1): # dequeue된 정점에서 갈 수 있는 모든 정점을 enqueue
            if adj_m[t][w] == 1 and visited[w] == 0:  # 인접한 정점 중 인큐되지 않은 정점이 있으면
                rear += 1   # enqueue
                Q[rear] = w # enqueue
                visited[w] = visited[t] + 1  # enqueue 표시(visited) 이렇게 하면 거리를 사용가능


"""
7 8 
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

V, E = map(int, input().split())  # 1번부터 V개의 정점, E개의 간선
arr = list(map(int, input().split()))

# 인접행렬
adj_m = [[0] * (V+1) for _ in range(V + 1)]

for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

print(adj_m)

bfs(1, V)
