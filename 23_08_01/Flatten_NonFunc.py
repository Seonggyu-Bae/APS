for test_case in range(1, 11):
    dump_count = int(input())
    box_height = list(map(int, input().split()))
    for i in range(dump_count):
        max_height = 0
        min_height = 100
        max_idx = 0
        min_idx = 0

        for idx, x in enumerate(box_height):
            if x > max_height:
                max_height = x
                max_idx = idx
            if x < min_height:
                min_height = x
                min_idx = idx

        if max_height == min_height:
            print(f'#{test_case} {max_height - min_height}')
            break
        else:
            box_height[min_idx] += 1
            box_height[max_idx] -= 1

    max_height = 0
    min_height = 100
    for x in box_height:
        if x > max_height:
            max_height = x
        if x < min_height:
            min_height = x

    print(f'#{test_case} {max_height - min_height}')
