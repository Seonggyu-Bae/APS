T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # 시계 방향으로 움직이는 델타 배열 생성
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # x,y: 현재 위치 idx
    # dir_v : 델타 배열 idx
    # num : 넣을 숫자
    x, y, dir_v, num = 0, 0, 0, 1
    snail = [[0] * N for _ in range(N)]

    while num <= N ** 2:
        snail[x][y] = num

        ndx, ndy = x + di[dir_v], y + dj[dir_v]
        # 다음 이동할 경로가 정상범위라면 그냥 가고 정상이 아니면 위치를 변경
        # 이것이 가능한 이유는 달팽이라는 규칙이 있기 때문임
        if ndx < 0 or ndx >= N or ndy < 0 or ndy >= N or snail[ndx][ndy] != 0:
            dir_v = (dir_v + 1) % 4

        x += di[dir_v]
        y += dj[dir_v]
        num += 1

    print(f"#{test_case}")
    for s in snail: print(*s)