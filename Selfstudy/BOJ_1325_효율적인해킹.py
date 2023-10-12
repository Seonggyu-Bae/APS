from collections import deque


def solve(start):
    cnt = 0
    q = deque([start])
    visited = [0] * (N + 1)
    visited[start] = 1

    while q:
        s = q.popleft()
        for x in trust[s]:
            if not visited[x]:
                q.append(x)
                visited[x] = 1
                cnt += 1
    return cnt


N, M = map(int, input().split())

trust = [[] * (N + 1) for _ in range(N + 1)]
how_many = [0] * (N + 1)
info = [list(map(int, input().split())) for _ in range(M)]
high = 0
ans = []

for num in info:
    a, b = num
    trust[b].append(a)


for i in range(1, N + 1):
    temp = solve(i)
    if temp > high:
        ans = [i]
        high = temp
    elif temp == high:
        ans.append(i)

print(*ans)
