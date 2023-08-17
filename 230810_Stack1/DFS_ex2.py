# 재귀로 구현
# 메모리 구조가 스택이기 때문에 코드가 간단해지는 편임
# v : 현재 위치(현재 정점)
def dfs2(v, visited, adj):
    visited[v] = 1
    print(v, end = ' ')
    for i in range(1, V+1):
        if adj[v][i] and not visited[i]:
            dfs2(i,visited,adj_matrix)



# Vertex(정점), Edge (간선)
V, E = map(int, input().split())

# 인접행렬
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    v1, v2 = map(int, input().split())
    adj_matrix[v1][v2], adj_matrix[v2][v1] = 1, 1

print(adj_matrix)

visited = [0]*(V+1)
dfs2(1,visited,adj_matrix)