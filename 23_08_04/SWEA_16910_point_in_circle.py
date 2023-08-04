T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    count = 0
    N_Square = N ** 2

    for i in range(1,N+2):
        count+=1

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if x ** 2 + y ** 2 <= N_Square:
                count += 1
    print(f'#{tc} {(count)*4 + 5}')
