for _ in range(10):
    T = int(input())
    left = False
    right = False
    ladder = [list(map(int, input().split())) for _ in range(100)]
    y = 99
    x = 0
    # 0 : 아래에서옴 1: 왼쪽에서옴 2:오른쪽에서 옴
    dir_i = 0
    for i in range(99):
        if ladder[99][i] == 2:
            x = i

    while y > 0:

        if (dir_i ==0 or dir_i == 1) and 1 < x < 99 and 1 < y < 99 and ladder[y][x-1]==1:
            x -= 1



        elif:


        else:




    print(f'#{T} {x}')
