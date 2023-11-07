import sys

from collections import deque


def solve(start, end):
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
            #
            # if not lineinfo[go] and go != end:
            #     print(not lineinfo[go])
            #     visited[go] = 0

    my_set = set()
    for idx, v in enumerate(visited):
        if v == 1 and idx != start and idx != end:
            my_set.add(idx)
    return my_set


# 방문한 정점에서 목적지 까지 갈 수 있는 방법이 있어야함


N, M = map(int, input().split())  # N: 정점, M: 간선의 개수

lineinfo = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    lineinfo[x].append(y)

S, T = map(int, input().split())

visited = [0] * (N + 1)

going = solve(S, T)
for x in going:
    print(solve(x,T))
print(going)
back = solve(T, S)
for x in back:
    print(solve(x,S))
print(back)
print(len(going.intersection(back)))
