import math

T = int(input())

for tc in range(1, T+1):
    M, N, x, y = map(int, input().split())
    # 카잉 달력의 마지막 해는 M과 N의 최소 공배수이다
    last_year = math.lcm(M, N)

    M_data = [x]
    M_len = 1
    N_data = [y]
    N_len = 1

    while M_data[M_len-1]+M <= last_year:
        M_data.append(M_data[M_len-1]+M)
        M_len += 1

    while N_data[N_len-1]+N <= last_year:
        N_data.append(N_data[N_len-1]+N)
        N_len += 1

    for x in M_data:
        if x in N_data:
            print(x)
            break
    else:
        print('-1')
