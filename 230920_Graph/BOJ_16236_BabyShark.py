from collections import deque

di = [1,-1,0,0]
dj = [0,0, 1, -1]

def find_baby_shark(n):
    for i in range(n):
        for j in range(n):
            if info[i][j] == 9:
                return i,j

def movingshark(n,x,y):
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    deQ = deque()
    deQ.append((x,y))
    shark_size = 2
    while deQ:
        ci,cj = deQ.popleft()

        for d in range(4):
            ni, nj = si+di[d], sj+dj[d]
            if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and info[ni][nj] <= shark_size:
                if shark_size > info[ni][nj]:
                    shark_size +=1
                    info[ni][nj] = 0
                visited[ni][nj] = visited[si][sj] + 1





N = int(input())

info = [list(map(int, input().split()) for _ in range(N))]
si,sj = find_baby_shark(N)

movingshark(N,si,sj)