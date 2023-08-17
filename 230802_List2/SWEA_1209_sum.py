for _ in range(10):
    max_sum = 0
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    temp_sum = 0
    # 1. 각 행의 합 확인
    for i in range(100):
        temp_sum = 0
        for j in range(100):
            temp_sum += data[i][j]
        if temp_sum > max_sum:
            max_sum = temp_sum

    # 2. 각 열의 합 확인
    for i in range(100):
        temp_sum = 0
        for j in range(100):
            temp_sum += data[j][i]
        if temp_sum > max_sum:
            max_sum = temp_sum

    # 3. 대각선 1
    temp_sum = 0
    for i in range(100):
        temp_sum += data[i][i]
    if temp_sum > max_sum:
        max_sum = temp_sum

    # 3. 대각선 2
    temp_sum = 0
    for i in range(100):
        temp_sum += data[i][99-i]
    if temp_sum > max_sum:
        max_sum = temp_sum


    print(f'#{tc} {max_sum}')