import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def findDOYeon():
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I':
                return i, j


def solve(sy, sx):
    visited = [[0] * M for _ in range(N)]
    visited[sy][sx] = 1
    q = deque([(sy, sx)])
    cnt = 0
    while q:
        i, j = q.popleft()
        for d in range(4):
            ni, nj = i + dy[d], j + dx[d]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and campus[ni][nj] != 'X':
                q.append((ni, nj))
                visited[ni][nj] = 1
                if campus[ni][nj] == 'P':
                    cnt += 1
    return cnt


N, M = map(int, input().split())

campus = [input().rstrip() for _ in range(N)]

y, x = findDOYeon()

ans = solve(y, x)
if ans:
    print(ans)
else:
    print('TT')
