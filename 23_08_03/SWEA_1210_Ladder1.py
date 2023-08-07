for _ in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    y = 99
    x = 0
    # dir_i =  0 : 아래에서옴 1: 왼쪽에서옴 2:오른쪽에서 옴
    dir_i = 0
    for i in range(100):
        if ladder[99][i] == 2:
            x = i

    while y > 0:

        if (dir_i == 0 or dir_i == 1) and x > 0 and ladder[y][x - 1]:
            x -= 1
            dir_i = 1

        elif (dir_i == 0 or dir_i == 2) and x < 99 and ladder[y][x + 1]:
            x += 1
            dir_i = 2
        else:
            y -= 1
            dir_i = 0

    print(f'#{T} {x}')
