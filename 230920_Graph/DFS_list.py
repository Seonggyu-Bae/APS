# 인접리스트
# 갈 수 있는 지점만 저장하자.
# 메모리사용이 인접 행렬에 비해 훨씬 효율적이다.
# 주의 사항
# 각 노드마다 갈 수 있는 지점의 개수가 다름
# 즉, range 사용 할 때 index 조심
graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3]
]


#  파이썬은 딕셔너리로도 구현할 수 있다.
# graph_dict = {
#     '0' : [1, 3],
#     '1' : [0, 2, 3, 4],
#     '2' : [1],
#     '3' : [0, 1, 4],
#     '4' : [1, 3]
# }


def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        current = stack.pop()
        # 이미 방문한 지점이라면 continue
        if current in visited:
            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(current)

        # 갈 수 있는 곳들을 stack에 추가
        for n_idx in range(len(graph[current]) - 1, -1, -1):  # range(len(graph))

            next_vertex = graph[current][n_idx]
            # 방문한 지점이라면 stack에 추가하지 않음
            if next_vertex in visited:
                continue

            stack.append(next_vertex)

    return visited


print("dfs stack = ", end='')
print(*dfs_stack(0))

visited = [0] * len(graph)
path = []  # 방문 순서 기록


def dfs_recur(now):
    visited[now] = 1  # 현재 지점 방문표시
    path.append(now)
    # 인접한 노드들 방문
    for next_idx in range(len(graph[now])):

        next_vertex = graph[now][next_idx]

        if visited[next_vertex]:
            continue

        dfs_recur(next_vertex)


dfs_recur(0)
print('dfs recur = ', end='')
print(*path)

# 인접리스트
