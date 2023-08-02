T = int(input())

for tc in range(1, T + 1):
    # 색칠할 배열 선언
    red = [[0] * 10 for _ in range(10)]
    blue = [[0] * 10 for _ in range(10)]

    # 보라색 카운트 할 변수 선언
    purple = 0
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]

    # info의 정보를 바탕으로 빨간색 배열, 파란색 배열에 색칠
    for i in range(N):
        # r1, c1, r2, c2, color = info[i]
        for color_i in range(info[i][0], info[i][2] + 1):
            for color_j in range(info[i][1], info[i][3] + 1):
                # 빨간색이면 빨간 배열에
                if info[i][4] == 1:
                    red[color_i][color_j] += 1
                # 파란색이면 파란 배열에
                else:
                    blue[color_i][color_j] += 1

    # 빨간색 파란색이 칠해져있는 배열이 겹치면 보라색 카운트 +1
    for i in range(10):
        for j in range(10):
            if red[i][j] != 0 and blue[i][j] != 0:
                purple += 1

    print(f'#{tc} {purple}')