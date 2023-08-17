T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    max_count = 0       # 각 테스트케이스마다 max count 가 초기화 되어야한다.

    # N X M 행렬 탐색
    for i in range(N):
        for j in range(M):
            count = 0           # 행렬의 각 요소를 검사할 때마다 count(꽃가루 수)는 초기화 해야함
            count += info[i][j] # 먼저 탐색할 요소의 꽃가루 수를 더해준다
            # 윗 두줄을 count = info[i][j]로 대체가능
            distance = info[i][j] # 꽃가루 수 만큼 상하좌우도 터지니까 거리를 정해준다
            for k in range(1, distance + 1): # 1 ~ 거리칸 만큼 터트려야함
                for l in range(4):              # 델타를 돌리기 위함
                    nx, ny = i + (dx[l] * k), j + (dy[l] * k) # 기존에 i + dx 였던것을 i + (dx*k)로 바꾸어 거리 반영 함
                    if 0 <= nx < N and 0 <= ny < M:           # 배열 인덱스를 넘어가지 않으면
                        count += info[nx][ny]                 # 꽃가루 수를 더해줌
            if count > max_count:                             # 거리만큼 다 돌렸으면 max_count 와 비교해서 더 크면 max_count를 바꿔준다.
                max_count = count

    print(f'#{tc} {max_count}')
