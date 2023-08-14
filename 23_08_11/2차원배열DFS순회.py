# (0, 0) 에서 시작해서 1이면 갈 수있고 0이면 못지나감 2가 출구임
# 2로 갈 수 있는지 확인하는것이 목표임

arr = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 2],
]

N = 5


def dfs():
    # (0, 0) 시작 노드
    # 방문 표시 배열도 2차원 배열로 만들어야함
    stack = [(0, 0)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1

    # 현재 위치에서 갈 수 있는 길 찾아보기 >> 반복
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while stack:
        """
        current = stack[-1]
        current[0]
        current[1]
        """
        cr, cc = stack[-1]
        if arr[cr][cc] == 2:
            return 1
        #  현재 위치에서 갈 수 있는 길 찾기
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and \
                    arr[nr][nc] != 0 and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                break
        else:
            stack.pop()

    return 0


print(dfs())
