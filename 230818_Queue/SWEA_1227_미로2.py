def find_startpoint():
    for i in range(100):
        for j in range(100):
            if map_info[i][j] == '2':
                return i, j
    return -1, -1

def find_endpoint(si,sj):
    visited = [[0] * 100 for _ in range(100)]
    visited[si][sj] = 1
    Q = [(si,sj)]

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    while Q:
        ci, cj = Q.pop(0)
        if map_info[ci][cj] == '3':
            return 1

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < 100 and 0 <= nj < 100 and not visited[ni][nj] and map_info[ni][nj] != '1':
                Q.append((ni, nj))
                visited[ni][nj] = 1
    return 0


for _ in range(10):
    tc = int(input())
    map_info = [list(input()) for _ in range(100)]

    si, sj = find_startpoint()

    ans = find_endpoint(si,sj)
    """
       if si == sj == -1:
           print('there is no startpoint in maze')
           ans = 0
    """
    print(f'#{tc} {ans}')