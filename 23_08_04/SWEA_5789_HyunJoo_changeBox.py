T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    my_box = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())

        for box_idx in range(L-1, R):
            my_box[box_idx] = i

    print(f'#{tc}', *my_box)
