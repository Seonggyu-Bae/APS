T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    Alist = list(map(int,input().split()))
    max = Alist[0]
    min = Alist[0]
    for num in Alist:
        if max < num:
            max = num
        if min > num:
            min = num
    print(f'#{test_case} {max-min}')    