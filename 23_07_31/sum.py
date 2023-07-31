T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int,(input().split()))
    Alist = list(map(int, input().split()))
    min_sum = 0
    max_sum = 0
    
    for i in range(0,N-M+1):
        sum = 0
        for j in range(M):
            sum += Alist[i+j]

        if i == 0:
            min_sum = sum
            max_sum = sum

        if min_sum > sum:
            min_sum = sum
        if max_sum < sum:
            max_sum = sum        


    print(f'#{test_case} {max_sum-min_sum}')        


