import sys

from collections import deque


def solve(start, end):
    visited = [0] * (N + 1)

    q = deque()
    q.append(start)
    while q:
        s = q.popleft()
        if s == end:
            continue
        for go in lineinfo[s]:
            if not visited[go]:
                q.append(go)
                visited[go] = 1
            if not lineinfo[go] and go != end:
                visited[go] = 0

    my_set = set()
    for idx, v in enumerate(visited):
        if v == 1 and idx != start and idx != end:
            my_set.add(idx)
    return my_set


N, M = map(int, input().split())  # N: 정점, M: 간선의 개수

# lineinfo = [[0] * (N + 1) for _ in range(N + 1)]
lineinfo = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    lineinfo[x].append(y)

S, T = map(int, input().split())


going = solve(S, T)
back = solve(T, S)
print(len(going.intersection(back)))
