from collections import deque


def solve(start, want):
    deQ = deque()
    deQ.append(start)
    visited = [0] * 1000001
    visited[start] = 1
    while deQ:
        now = deQ.popleft()
        if now == want:
            return visited[now]
        if 0 <= now + 1 <= 1000000 and not visited[now + 1]:
            deQ.append(now + 1)
            visited[now + 1] = visited[now] + 1
        if 0 <= now - 1 <= 1000000 and not visited[now - 1]:
            deQ.append(now - 1)
            visited[now - 1] = visited[now] + 1
        if 0 <= now * 2 <= 1000000 and not visited[now * 2]:
            deQ.append(now * 2)
            visited[now * 2] = visited[now] + 1
        if 0 <= now - 10 <= 1000000 and not visited[now - 10]:
            deQ.append(now - 10)
            visited[now - 10] = visited[now] + 1


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    ans = 0
    if N > M:
        ans += (N - M) // 10 + (N - M) % 10
        print(f'#{tc} {ans}')
    else:
        ans += solve(N, M)
        print(f'#{tc} {ans - 1}')
