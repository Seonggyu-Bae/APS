T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    count = 0
    N_Square = N ** 2

    # 축과 원점을 제외하고 원안에 있는 1사분면에 있는 점을구하고
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if x ** 2 + y ** 2 <= N_Square:
                count += 1
    # 4개 곱하고
    count *= 4
    # 축 4개 더해주고 중복된 원점 빼주기
    count += (N + 1) * 4 - 3

    # 아래는 완탐
    """for x in range(-N, N + 1):
        for y in range(-N, N + 1):
            if x ** 2 + y ** 2 <= N_Square:
                count += 1"""

    print(f'#{tc} {count}')
