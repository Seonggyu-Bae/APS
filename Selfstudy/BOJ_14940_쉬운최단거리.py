import sys
from collections import deque


input = sys.stdin.readline


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def solve(ti, tj):
    visited[ti][tj] = 1
    q = deque([(ti, tj)])
    while q:
        si, sj = q.popleft()
        for d in range(4):
            ni, nj = si + di[d], sj + dj[d]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and land_info[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = visited[si][sj] + 1


def find_target_place():
    for i in range(N):
        for j in range(M):
            if land_info[i][j] == 2:
                return i, j


def check():
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                if land_info[i][j] == 1:
                    visited[i][j] = -1
            else:
                visited[i][j] -= 1


N, M = map(int, input().split())

land_info = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
solve(*find_target_place())
check()
for distance in visited:
    print(*distance)
