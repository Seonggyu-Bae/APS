T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = list(map(int,input().split()))

    num_max = arr[0]
    num_min = arr[0]

    for num in arr:
        if num_max < num:
            num_max = num
        if num_min > num:
            num_min = num

    print(f'#{test_case} {num_max-num_min}')