def my_bfs(si, sj, N):          # 시작점(si,sj)과 미로의 크기(N X N)
    visited = [[0] * N for _ in range(N)]
    Q = [(si, sj)]
    visited[si][sj] = 1

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    while Q:
        i, j = Q.pop(0)
        if map_info[i][j] == 3:     # 도착지라면
            return visited[i][j] - 2    # 지나온 통로의 수를 출력하니까 -2 를 해줌

        # 현재위치와 인접(상하좌우)하고 enqueue된 적이 없으면
        # enqueue, enqueue 표시
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and map_info[ni][nj] != 1 and visited[ni][nj] == 0:
                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    return 0  # 경로가 없는 경우 0을 반환


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    map_info = [list(map(int, input())) for _ in range(N)]
    # 0은 통로, 1은 벽, 2는 출발점, 3은 도착점

    # 시작점 찾기
    si, sj = 0, 0
    for i in range(N):
        for j in range(N):
            if map_info[i][j] == 2:
                si, sj = i, j
                break

    ans = my_bfs(si, sj, N)
    print(f'#{tc} {ans}')
