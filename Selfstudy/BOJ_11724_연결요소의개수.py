from collections import deque
from sys import stdin


def solve(s):
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        start = q.popleft()
        for i in range(1, N + 1):
            if info[start][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = 1


N, M = map(int, input().split())

info = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
visited[0] = 1
for _ in range(M):
    s, i = map(int, stdin.readline().rstrip().split())
    info[s][i] = 1
    info[i][s] = 1
ans = 0

for x in range(1, N + 1):
    if not visited[x]:
        ans += 1
        solve(x)

print(ans)
