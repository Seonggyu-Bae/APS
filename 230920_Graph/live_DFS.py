# 인접행렬
# 장점 : 구현이 쉽다.
# 단점 : 메모리 낭비 -> 0도 표시를 하기 때문에
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

# if graph[start][want_to_go] == 1:
    # can go
# DFS
# 스택 OR 재귀로 구현
def dfs_stack(start):
    visited = []
    stack =[start]
    
    while stack:
        current = stack.pop()
        # 이미 방문한 지점이라면 continue
        if current in visited:
            continue
        
        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(current)
        
        # 갈 수 있는 곳들을 stack에 추가
        for next_vertex in range(len(graph)-1, -1, -1): # range(len(graph))
            # 연결이 안되어 있다면 continue
            if graph[current][next_vertex] == 0:
                continue

            # 방문한 지점이라면 stack에 추가하지 않음
            if next_vertex in visited:
                continue

            stack.append(next_vertex)

    return visited


print("dfs stack = ", end='')
print(*dfs_stack(0))


# DFS - 재귀
# MAP 크기(길이)를 알 때 구현가능
# 위의 스택으로 구현한 코드의 append, in은 속도가 느린편이다.

visited = [0] * len(graph)
path = [] # 방문 순서 기록

def dfs_recur(start):
    visited[start] = 1  # 현재 지점 방문표시
    path.append(start)
    # 인접한 노드들 방문
    for next_vertex in range(len(graph)):
        if graph[start][next_vertex] == 0:
            continue

        if visited[next_vertex]:
            continue

        dfs_recur(next_vertex)

dfs_recur(0)
print('dfs recur = ', end='')
print(*path)

# 인접리스트