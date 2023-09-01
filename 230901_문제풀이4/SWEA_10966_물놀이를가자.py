# 인덱스를 쓰던지 데큐를 쓰던지하자.
from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def my_bfs(n, m):  # 크기(N X M)
    global ans
    while water:
        i, j = water.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                ans += visited[ni][nj]-1  # 거리를 바로 더해준다 근데 처음주어진물이 1이라고 되어있어서 1빼줌.
                water.append((ni, nj))

    return


# 지도에서 물을 찾는 함수
def find_water():
    for i in range(N):
        for j in range(M):
            if map_info[i][j] == 'W':
                water.append((i, j))
                visited[i][j] = 1


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    map_info = [input() for _ in range(N)]

    water = deque() # 물의 위치를 담을 데큐
    visited = [[0] * M for _ in range(N)]   # 방문표시 및 물과의 거리를 더해줄 배열
    find_water()
    ans = 0

    my_bfs(N, M)
    print(f'#{tc} {ans}')
