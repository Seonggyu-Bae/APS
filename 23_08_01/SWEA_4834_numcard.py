T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_card = list(map(int,input()))
    count = [0] * 10

    for i in num_card:
        count[i] += 1

    max_count = 0
    max_num = 0

    for i in range(len(count)):
        if max_count <= count[i]:
            max_count = count[i]
            max_num = i

    print(f'#{test_case} {max_num} {max_count}')