def bfs(start):
    visited = [0] * 101
    visited[start] = 1
    Q = [start]

    while Q:
        t = Q.pop(0)
        for idx, c in enumerate(adj_l[t]):
            if c == 1 and not visited[idx]:     # 연락이 가능하고 연락하지 않았다면
                Q.append(idx)
                visited[idx] = visited[t] + 1   # 몇번째에 연락을 받았는지 저장

    last = 0
    last_idx = 0

    for i in range(100, 0, -1):
        if visited[i] > last:       # visited를 돌면서 숫자가 제일 큰 놈을 찾으면됨
            last = visited[i]
            last_idx = i

    return last_idx


for tc in range(1, 11):
    data_len, start = map(int, input().split())
    edge_info = list(map(int, input().split())) # 비상연락망 정보

    adj_l = [[0] * 101 for _ in range(101)]     # 인접리스트

    # 방향성이 있는 간선임에 유의하여 정보 저장
    for i in range(0, data_len, 2):
        adj_l[edge_info[i]][edge_info[i + 1]] = 1

    ans = bfs(start)

    print(f'#{tc} {ans}')
