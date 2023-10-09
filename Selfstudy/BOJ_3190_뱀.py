from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


# 상 하 좌 우

def solve(si, sj):
    s_dir = 3
    cnt = 1
    temp = 0
    i, j = si, sj
    tail = deque()
    tail.append((si,sj))
    while True:

        ni, nj = i + di[s_dir], j + dj[s_dir]

        # 1. 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
        if not (0 <= ni < N and 0 <= nj < N):
            return cnt
        elif board[ni][nj] == 1:
            return cnt
        # 2. 이동한 칸에 사과가 있다면 사과가 없어지고 꼬리는 움직이지 않는다.
        elif board[ni][nj] == 2:
            board[ni][nj] = 1
            tail.append((ni,nj))
            i, j = ni, nj
        # 3. 이동한칸에 사과가 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
        else:
            if tail:
                tail_i, tail_j = tail.popleft()
                board[tail_i][tail_j] = 0
            board[ni][nj] = 1
            tail.append((ni,nj))
            i, j = ni, nj

        if temp < L and str(cnt) == dir_info[temp][0]:

            if dir_info[temp][1] == 'D':
                if s_dir == 0:
                    s_dir = 3
                elif s_dir == 1:
                    s_dir = 2
                elif s_dir == 2:
                    s_dir = 0
                else:
                    s_dir = 1
            else:
                if s_dir == 0:
                    s_dir = 2
                elif s_dir == 1:
                    s_dir = 3
                elif s_dir == 2:
                    s_dir = 1
                else:
                    s_dir = 0
            temp += 1
        cnt += 1


N = int(input())  # NXN 보드
K = int(input())  # 사과의 개수
apple = [list(map(int, input().split())) for _ in range(K)]  # 사과의 위치 [행,열]
L = int(input())  # 뱀의 방향 변환 횟수
dir_info = [list(input().split()) for _ in range(L)]  # 방향 변환 정보 [초, 방향]

board = [[0] * N for _ in range(N)]
board[0][0] = 1

for info in apple:
    i, j = info
    board[i - 1][j - 1] = 2

print(solve(0, 0))
