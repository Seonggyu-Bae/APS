import sys

from collections import deque


def solve(start, end):
    visited = [0] * (N+1)

    q = deque()
    q.append(start)
    while q:
        s = q.popleft()
        if s == end:
            break
        for go in range(N+1):
            if lineinfo[s][go]:
                q.append(go)
                if go != start:
                    visited[go] = 1
            elif go == N:
                visited[go] = 0

    my_set = set()
    for idx, v in enumerate(visited):
        if v == 1 and idx != start and idx != end:
            my_set.add(idx)
    return my_set


N, M = map(int, input().split())  # N: 정점, M: 간선의 개수

lineinfo = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    lineinfo[x][y] = 1

S, T = map(int, input().split())


going = solve(S, T)
back = solve(T, S)

print(len(going.intersection(back)))
