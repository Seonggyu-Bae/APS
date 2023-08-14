def my_dfs(N, startpoint,info):

    my_stack = [(startpoint[0], startpoint[1])]
    # 방문 표시 배열도 2차원 배열로 만들어야함
    visited = [[0] * N for _ in range(N)]
    visited[startpoint[0]][startpoint[1]] = 1

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    while my_stack:
        ci, cj = my_stack[-1]
        if info[ci][cj] == 3:
            return 1
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            if 0 <= ni < N and 0 <= nj < N and \
                    info[ni][nj] != 1 and not visited[ni][nj]:
                my_stack.append((ni, nj))
                visited[ni][nj] = 1
                break
        else:
            my_stack.pop()
    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    map_info = [list(map(int, input())) for _ in range(N)]
    print(map_info)
    start = [0,0]

    for i in range(N):
        for j in range(N):
            if map_info[i][j] == 2:
                start[0],start[1] = i,j
                break

    print(f'#{tc} {my_dfs(N,start,map_info)}')
