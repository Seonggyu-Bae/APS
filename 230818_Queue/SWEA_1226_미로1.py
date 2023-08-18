def find_exit(si, sj):                          # 출발점을 인자로 받음
    visited = [[0] * 16 for _ in range(16)]     # 16 X 16 배열의 방문확인 배열
    visited[si][sj] = 1                         # 시작점 방문 표시
    Q = [(si, sj)]                              # 시작점을 큐에 넣고 시작

    di = [1, -1, 0, 0]                          # 현재 노드의 상하좌우를 탐색할 델타 배열
    dj = [0, 0, 1, -1]

    while Q:                                    # Q가 빌때까지 반복
        ci, cj = Q.pop(0)                       # Q의 첫번째 꺼내서
        if map_info[ci][cj] == '3':             # 그 점이 도착점이라면
            return 1                            # 갈 수 있다

        for d in range(4):                      # 아니면 인접경로(상하좌우) 탐색
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < 16 and 0 <= nj < 16 and not visited[ni][nj] and map_info[ni][nj] != '1':
                # 인접경로가 16X16 배열에 속하고 그 경로를 방문한적 없고 벽('1')이 아니라면
                Q.append((ni, nj))      # Q에 추가 해놓기
                visited[ni][nj] = 1     # 방문처리 해놓기

    return 0                            # 여기까지 오면 갈 수 있는 방법이 없는것임


def find_start():       # 16 X 16 미로에서 출발점을 찾는함수
    for i in range(16):
        for j in range(16):
            if map_info[i][j] == '2':
                return i, j


for _ in range(10):
    tc = int(input())

    map_info = [list(input()) for _ in range(16)]
    si, sj = find_start()

    ans = find_exit(si, sj)

    print(f'#{tc} {ans}')
