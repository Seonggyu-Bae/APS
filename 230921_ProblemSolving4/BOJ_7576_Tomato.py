from sys import stdin
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def solve(tomatoes):
    Q = deque((p[0], p[1]) for p in tomatoes)

    while Q:
        si, sj = Q.popleft()

        for d in range(4):
            ni, nj = si + di[d], sj + dj[d]
            if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj] and tomato_info[ni][nj] != -1:
                visited[ni][nj] = visited[si][sj] + 1
                Q.append((ni, nj))


def solve2():
    for i in range(M):
        for j in range(N):
            if visited[i][j] == 0 and tomato_info[i][j] == 0:
                return True


N, M = map(int, input().split())

tomato_info = [list(map(int, stdin.readline().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
ripe_tomato = []

# 익은 토마토의 좌표를 찾아서 ripe_tomato 에 저장
for i in range(M):
    for j in range(N):
        if tomato_info[i][j] == 1:
            visited[i][j] = 1
            ripe_tomato.append((i, j))

# 익은 토마토의 좌표들을 BFS 돌릴 함수에 넘겨줌
solve(ripe_tomato)


ans = 0
if solve2():
    ans = -1
else:
    ans = max([max(row) for row in visited]) -1

print(ans)

