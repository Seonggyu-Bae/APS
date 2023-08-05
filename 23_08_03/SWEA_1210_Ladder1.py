for _ in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    y = 99
    x = 0

    dir_i = 0                       # 0 : 아래에서옴 1: 왼쪽에서옴 2:오른쪽에서 옴
    for i in range(100):
        if ladder[99][i] == 2:      #2를 찾음
            x = i

    while y > 0:                    #출발지갈때까지 반복
        if (dir_i == 0 or dir_i == 1) and x > 0 and ladder[y][x - 1]:       #이전에 온 곳이 아래거나 왼쪽이고 왼쪽이 연결되어있을때
            x -= 1
            dir_i = 1
        elif (dir_i == 0 or dir_i == 2) and x < 99 and ladder[y][x + 1]:    #이전에 온 곳이 아래거나 오른쪽이고 오른쪽이 연결되어있을때
            x += 1
            dir_i = 2
        else:
            y -= 1
            dir_i = 0

    print(f'#{T} {x}')
