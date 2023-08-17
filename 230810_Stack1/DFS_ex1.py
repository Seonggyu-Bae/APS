# 깊이 우선 탐색(DFS: Depth First Search)
# 그래프 순회
# 그래프를 표현하는 방법은?
# 노드들 간의 연결 정보를 표시하기 위해
# 행렬을 사용할것이다.

# 정점(노드)가 7개이고, 1번부터 7번까지 있다면
# 8 X 8 행렬을 만든다

# Vertex(정점), Edge (간선)
V, E = map(int, input().split())

# 인접행렬
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(E):
    v1, v2 = map(int, input().split())
    adj_matrix[v1][v2], adj_matrix[v2][v1] = 1, 1

print(adj_matrix)


# DFS 시작
# 정점에서 연결된 모든 정점을 다 방문할것임 (방문했던 정점은 다시 방문하지 않음)
# 연결이 되어 있다면 방문
# 방문한 정점에서 더 이상 갈 수있는 정점이 없으면
# 이전으로 되돌아가서 다시 시작

# start : 시작정점 , adj : 연결정보
def my_dfs(start, adj):
    # 방문했던 정점은 다시 방문하지 않음
    visited = [0] * (V+1)   # 방문 여부 표시

    # 경로 저장을 위한 자료구조가 필요함 (스택으로 만듬)
    # 시작지점 경로추가 및 방문표시
    stack = [start]
    visited[start] = 1
    print(start, end=' ')
    # 현재 있는 위치에서 길찾기
    # 현재 위치에서 갈 수 있는 길이 없으면? -> 되돌아가기
    # 경로상에 정점이 남아있으면 -> 계속해서 탐색
    while stack:
        # 경로상에 마지막에 방문한 정점에서 길찾기
        top = stack[-1]

        # 방문한곳 표시
        visited[top] = 1
        # 어떤 정점과 연결된 모든 정점 방문하기
        # adj[top] : top과 연결된 정점들의 정보
        # adj[top]을 순회하면서 연결되어 있는 애들 찾기
        for i in range(V+1):
            # 참이면 top이랑 i번이랑 연결
            if adj[top][i] == 1 and not visited[i]:
                print(i,end=' ')
                stack.append(i)     # 길이 있으니 경로 추가
                break               # 길찾았으니까 방문

        else:                       # if에 안걸렸으면(길 못찾았으면)
            stack.pop()
    print()


my_dfs(1,adj_matrix)