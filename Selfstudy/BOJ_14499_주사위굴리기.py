di = [0, 0, 0, -1, 1]
dj = [0, -1, 1, 0, 0]

def solve(i,j):
    dice = [0] * 6
    top = 0
    bottom = 5
    si,sj = i,j
    for d in command:
        ni,nj = si+di[d], sj+dj[d]
        if 0<=ni<N and 0<= nj < M:
            if d == 1 and top == 0:
                top = 3
                bottom = 2
            if d == 2 and top == 0:
                top = 2
                bottom = 3
            if d == 3 and top == 0:
                top = 4
                bottom = 1
            if d == 4 and top == 0:
                top = 1
                bottom = 4
            if d == 1 and top == 1:
                


import sys

input = sys.stdin.readline

N, M, x, y, k = map(int, input().split())

map_num = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

solve(y,x)
