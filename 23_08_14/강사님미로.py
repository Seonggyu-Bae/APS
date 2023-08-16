dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 현재 위치에서 길 찾기

def dfs(r, c, visited):
    if maze[r][c] == 3:  # 목적지 도착가능
        return 1
    visited[r][c] = 1
    # 4방향 탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            # maze[nr][nc]가 벽(1)이아니고, 방문하지 않았으면 방문
            if maze[nr][nc] != 1 and not visited[nr][nc]:
                if dfs(nr, nc, visited) == 1:
                    return 1

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    maze = [list(map(int, input().strip())) for _ in range(N)]
    print(maze)
    visited = [[0] * N for _ in range(N)]
    r,c = 0,0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
                break

    print(f'#{tc} {dfs(r, c, visited)}')
