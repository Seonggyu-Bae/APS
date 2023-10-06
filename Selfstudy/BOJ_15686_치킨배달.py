from collections import deque
from itertools import combinations

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def solve(idx):
    q = deque()
    for c in choose[idx]:
        y, x = c
        q.append((y, x))
        visited[y][x] = 1

    while q:
        si, sj = q.popleft()
        for d in range(4):
            ni, nj = si + di[d], sj + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = visited[si][sj] + 1
                q.append((ni, nj))


N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]
chi = []
house = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chi.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))


ans = 0xfffffff
choose = list(combinations(chi, M))

for i in range(len(choose)):
    visited = [[0] * N for _ in range(N)]
    solve(i)
    temp = 0

    for x in house:
        i, j = x
        temp += visited[i][j] - 1
    if temp < ans:
        ans = temp

print(ans)
