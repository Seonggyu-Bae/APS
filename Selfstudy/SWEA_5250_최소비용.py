from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def solve(y, x):
    q = deque()
    q.append((y,x))
    visited = [[0xfffffff] * N for _ in range(N)]
    visited[y][x] = 0

    while q:
        si, sj = q.popleft()
        for d in range(4):
            ni, nj = si + di[d], sj + dj[d]
            if 0<=ni<N and 0<=nj<N:
                diff = info[ni][nj] - info[si][sj]
                temp =0
                if diff > 0:
                    temp = diff + visited[si][sj] +1
                else:
                    temp = visited[si][sj] +1
                if temp < visited[ni][nj]:
                    visited[ni][nj] = temp
                    q.append((ni,nj))
    return visited[N-1][N-1]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    info = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {solve(0,0)}')