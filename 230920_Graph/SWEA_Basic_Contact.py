from collections import deque
def bfs(s):
    deQ = deque()
    deQ.append(s)
    visited = [0] * 101
    visited[s] = 1

    while deQ:
        now = deQ.popleft()

        for v in adj_list[now]:
            if not visited[v]:
                deQ.append(v)
                visited[v] = visited[now] + 1

    return visited

for tc in range(1,11):
    data_len, start = map(int, input().split())
    data = list(map(int, input().split()))
    adj_list = [set() for _ in range(101)]
    for i in range(0,data_len,2):
        adj_list[data[i]].add(data[i+1])


    ans_list = bfs(start)
    ans = 0
    ans_idx = 0

    for i in range(1,101):
        if ans <= ans_list[i]:
            ans = ans_list[i]
            ans_idx = i
    print(f'#{tc} {ans_idx}')