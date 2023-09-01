from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

t_dir = {1: [0, 1, 2, 3], 2: [0, 1], 3: [2, 3],
         4: [1, 2], 5: [0, 2], 6: [0, 3], 7: [1, 3]
         }


# 하 상 우 좌

def my_bfs(si, sj):
    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1
    deq = deque()
    deq.append((si, sj))

    while deq:
        i, j = deq.popleft()
        for d in t_dir[tunnel_info[i][j]]:
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and tunnel_info[ni][nj] and not visited[ni][nj]:
                if d == 0:  # 하를 탐색할때는 상이 있으면 연결됨
                    if 1 in t_dir[tunnel_info[ni][nj]]:
                        visited[ni][nj] = visited[i][j] + 1
                        deq.append((ni, nj))
                elif d == 1:  # 상을 탐색할때는 하가 있으면 연결됨
                    if 0 in t_dir[tunnel_info[ni][nj]]:
                        visited[ni][nj] = visited[i][j] + 1
                        deq.append((ni, nj))
                elif d == 2:  # 우를 탐색할때는 좌가 있으면 연결됨
                    if 3 in t_dir[tunnel_info[ni][nj]]:
                        visited[ni][nj] = visited[i][j] + 1
                        deq.append((ni, nj))
                else:  # 좌을 탐색할때는 우가 있으면 연결됨
                    if 2 in t_dir[tunnel_info[ni][nj]]:
                        visited[ni][nj] = visited[i][j] + 1
                        deq.append((ni, nj))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] < L + 1:
                cnt += 1
    return cnt


T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    # 지하 터널 지도의 세로 크기 N, 가로 크기 M
    # 맨홀 뚜껑의 세로 위치 R 가로 위치 C
    # 탈출 후 소요된 시간 L
    tunnel_info = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {my_bfs(R, C)}')
