from collections import deque


def solve():
    visited = [0] * 100
    visited[0] = 1
    q = deque()
    q.append(0)
    while q:
        now = q.popleft()
        if now == 99:
            return visited[99] -1
        for i in range(1, 7):
            if i + now < 100:
                if not visited[i + now]:
                    q.append(board[i + now])
                    visited[i + now] = visited[now] + 1
                    visited[board[i + now]] = visited[now] + 1


N, M = map(int, input().split())

ladder_info = [list(map(int, input().split())) for _ in range(N)]
snake_info = [list(map(int, input().split())) for _ in range(M)]

board = [x for x in range(100)]

for infos in ladder_info:
    now, go = infos
    board[now - 1] = go - 1

for infos in snake_info:
    now, go = infos
    board[now - 1] = go - 1

print(solve())
