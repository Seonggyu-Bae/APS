from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

# 현재 아기 상어보다 작은 물고기들
def find_fish(x,y):
    global shark_size
    fish = deque()
    for i in range(N):
        for j in range(N):
            if 1 <= info[i][j] < shark_size:
                fish.append((i, j))
    min_dis = 0xfffffff
    for i in range(len(fish)):
        temp = abs(fish[i][0]-x) + abs(fish[i][1]-y)
        if temp < min_dis:
            min_dis


# 아기 상어 위치
def find_baby_shark(n):
    for i in range(n):
        for j in range(n):
            if info[i][j] == 9:
                return i, j


def moving_shark(n, x, y):
    global shark_size
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    deQ = deque()
    deQ.append((x, y))

    while deQ:
        ci, cj = deQ.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and info[ni][nj] <= shark_size:
                if info[ni][nj] != 0 and shark_size > info[ni][nj]:
                    shark_size += 1
                    info[ni][nj] = 0
                visited[ni][nj] = visited[ci][cj] + 1


# 아기상어가 갈 수 있는 위치까지의 거리
def find_dist(x, y):
    global shark_size
    fish_distance[x][y] = 1
    deQ = deque()
    deQ.append((x, y))

    while deQ:
        ci, cj = deQ.popleft()

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < N and 0 <= nj < N and not fish_distance[ni][nj] and info[ni][nj] <= shark_size:
                fish_distance[ni][nj] = fish_distance[ci][cj] + 1
                deQ.append((ni, nj))


N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]

si, sj = find_baby_shark(N)
shark_size = 2

fish_distance = [[0] * N for _ in range(N)]

find_fish()
find_dist(si, sj)

print(fish_distance)
print(*fish)
# moving_shark(N, si, sj)
