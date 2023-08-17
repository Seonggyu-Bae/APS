"""
V E
v1 w1 v2 w2 ....
7 8

1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
def dfs(n, V, adj_m):
    stack = []              # 1. stack 생성
    visited = [0] * (V+1)   # 2. visited 생성
    visited[n] = 1          # 3. 시작점 방문 표시
    print(n)                # 4. do[n]
    while True:
        for w in range(1,V+1):  # 1. 현재 정점 n에 인접하고 미방문한 w 찾기
                if adj_m[n][w] == 1 and visited[w] == 0:
                    stack.append(n)     # push(n)v = w
                    n = w               # v = w
                    print(n)            # do(w)
                    visited[n] = 1      # w 방문 표시
                    break               # for w, n에 인접인 w 찾은경우
        else:
            if stack:           # 스택에 지나온 정점이 남아있으면
                n = stack.pop() # pop() 해서 다시 다른 w 찾을 n 준비
            else:               # 스택이 비어있으면
                break           # while True 탐색 끝

    return





# 1번부터 V번 정점, E개의 간선
V, E = map(int, input().split())

# 입력받올 간선 정보
edges = list(map(int,input().split()))

# 간선의 정보를 저장할 배열
adj_matrix = [[0] * (V+1) for _ in range(V+1)]

# 이어져 있는지 여부를 확인하는 matrix 생성
for i in range(E):
    v1, v2 = edges[i*2], edges[i*2+1]
    adj_matrix[v1][v2] = 1
    adj_matrix[v2][v1] = 1

"""
for i in range(0,E*2,2):
    adj_matrix[edges[i]][edges[i+1]] = 1
    adj_matrix[edges[i+1]][edges[i]] = 1
"""

dfs(1,V,adj_matrix)
