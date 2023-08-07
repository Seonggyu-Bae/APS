import math

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    i, j = 0, 0
    for k in range(1, int(math.sqrt(N)) + 1):
        if N % k == 0:
            i = k
            j = N // k

    print(f'#{tc} {i + j - 2}')
