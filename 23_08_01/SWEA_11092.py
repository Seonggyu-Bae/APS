T = int(input())

for tc in range(1,T+1):
    N = int(input())
    my_list = list(map(int, input().split()))

    num_max = 0
    num_min = 10
    idx_max = 0
    idx_min = 0

    """
    강사님 풀이 내 풀이보다 변수를 2개를 줄였다.
    더 좋은것 같다.
    min_idx = 0
    max_idx = 0
    for i in range(1,N):
        if my_list[min_idx] > arr[i]:
            min_idx = i
        if my_list[max_idx] < arr[i]
            max_idx = i
            
    if max_idx > min_idx:
        print(f'#{tc} {idx_max - idx_min}')
    else:
        print(f'#{tc} {idx_min - idx_max}')

    """
    for idx, num in enumerate(my_list):
        if num >= num_max:
            num_max = num
            idx_max = idx
        if num < num_min:
            num_min = num
            idx_min = idx

    if idx_max > idx_min:
        print(f'#{tc} {idx_max - idx_min}')
    else:
        print(f'#{tc} {idx_min - idx_max}')
