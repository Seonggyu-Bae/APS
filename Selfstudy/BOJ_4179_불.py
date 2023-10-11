di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
from collections import deque


def solve():
    q = deque(jihoon+fire)
    # for x in jihoon:
    #     q.append(x)
    #     visited[x[0]][x[1]] = 1
    #
    # for f in fire:
    #     q.append(f)
    #     visited[f[0]][f[1]] = 1
    #     fire_visited[f[0]][f[1]] = 1

    while q:
        if not a:
            break
        si, sj = q.popleft()
        if maze[si][sj] == 'J':
            if si == 0 or si == R - 1 or sj == 0 or sj == C - 1:
                return visited[si][sj]
            for d in range(4):
                ni, nj = si + di[d], sj + dj[d]
                if 0 <= ni < R and 0 <= nj < C and maze[ni][nj] != '#' and maze[ni][nj] != 'F' and not visited[ni][nj]:
                    visited[ni][nj] = visited[si][sj] + 1
                    q.append((ni, nj))
                    maze[ni][nj] = 'J'
            maze[si][sj] = '.'

        if maze[si][sj] == 'F':
            for d in range(4):
                ni, nj = si + di[d], sj + dj[d]
                if 0 <= ni < R and 0 <= nj < C and maze[ni][nj] != '#' and not fire_visited[ni][nj]:
                    fire_visited[ni][nj] = 1
                    visited[ni][nj] = visited[si][sj] + 1
                    q.append((ni, nj))
                    maze[ni][nj] = 'F'

    return 'IMPOSSIBLE'


def findjihoonandfire():
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
                jihoon.append((i, j))
                visited[i][j] = 1
            elif maze[i][j] == 'F':
                fire.append((i, j))
                visited[i][j] = 1
                fire_visited[i][j] = 1


def a():
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
                return True
    return False


R, C = map(int, input().split())

maze = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
fire_visited = [[0] * C for _ in range(R)]
jihoon = []
fire = []
findjihoonandfire()
a = solve()
print(a)
