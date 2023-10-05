from itertools import combinations
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def solve():
    chk = 0
    visited = [[0] * M for _ in range(N)]
    q = deque(virus)
    for x in virus:
        visited[x[0]][x[1]] = 1

    while q:
        si, sj = q.popleft()
        for d in range(4):
            ni, nj = si + di[d], sj + dj[d]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and info[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                chk += 1
    return chk


N, M = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(N)]
virus = []
empty = []

ans = 0

for i in range(N):
    for j in range(M):
        if info[i][j] == 2:
            virus.append((i, j))
        elif info[i][j] == 0:
            empty.append((i, j))

wall_list = list(combinations(empty, 3))
temp = N * M - len(empty) - len(virus) + 3

for i in range(len(wall_list)):
    info[wall_list[i][0][0]][wall_list[i][0][1]], info[wall_list[i][1][0]][wall_list[i][1][1]], \
    info[wall_list[i][2][0]][wall_list[i][2][1]] = 1, 1, 1
    if ans < N * M - solve() - temp:
        ans = N * M - solve() - temp
    info[wall_list[i][0][0]][wall_list[i][0][1]], info[wall_list[i][1][0]][wall_list[i][1][1]], \
    info[wall_list[i][2][0]][wall_list[i][2][1]] = 0, 0, 0

print(ans)
