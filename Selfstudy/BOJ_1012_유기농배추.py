from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def solve(si, sj):
    Q = deque()
    Q.append((sj, si))

    while Q:
        j, i = Q.popleft()

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and bachuland[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                Q.append((nj, ni))
                # x, y 잘 생각해야함


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    bachuland = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    bachuloc = [list(map(int, input().split())) for _ in range(K)]
    for i in range(K):
        bachuland[bachuloc[i][1]][bachuloc[i][0]] = 1

    ans = 0
    for i in range(N):
        for j in range(M):
            if bachuland[i][j] == 1:
                if visited[i][j] == 0:
                    ans += 1
                    visited[i][j] = 1
                solve(i, j)

    print(ans)
