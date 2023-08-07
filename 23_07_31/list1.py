T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    Alist = list(map(int, input().split()))
    max_v = 0
    min_v = 10000000

    for num in Alist:
        if max_v < num:
            max_v = num
        else:
            pass
        if min_v > num:
            min_v = num
        else:
            pass

    print(f'#{test_case} {max_v - min_v}')