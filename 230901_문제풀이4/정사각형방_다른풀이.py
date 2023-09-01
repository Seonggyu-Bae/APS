"""

N2개의 방이 N×N형태로 늘어서 있다.

위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며,
이 숫자는 모든 방에 대해 서로 다르다.

당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.

물론 이동하려는 방이 존재해야 하고,
이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.

처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하라.

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (1 ≤ N ≤ 103)이 주어진다.

다음 N개의 줄에는 i번째 줄에는 N개의 정수
Ai, 1, … , Ai, N (1 ≤ Ai, j ≤ N2) 이 공백 하나로 구분되어 주어진다.

Ai, j는 모두 서로 다른 수이다.

"""
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    info = [0] * (N * N + 1)
    max_cnt = 0
    max_v = 0

    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < N and 0 <= nj < N and room[ni][nj] == room[i][j] + 1:
                    info[room[i][j]] = 1
                    break
    cnt = 0
    for i in range(len(info) - 1, -1, -1):
        if info[i] == 1:
            cnt += 1
        if info[i] == 0:
            if cnt > max_cnt:
                max_cnt = cnt
                max_v = i + 1
            elif cnt == max_cnt and i < max_v:
                max_v = i + 1
            cnt = 0

    print(f'#{tc} {max_v} {max_cnt + 1}')
