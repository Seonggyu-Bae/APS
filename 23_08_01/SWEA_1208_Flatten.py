for test_case in range(1, 11):
    dump_count = int(input())
    box_height = list(map(int, input().split()))

    for _ in range(dump_count):
        max_idx = box_height.index(max(box_height))
        min_idx = box_height.index(min(box_height))

        if max(box_height) == min(box_height):
            break
        else:
            box_height[min_idx] += 1
            box_height[max_idx] -= 1

    print(f'#{test_case} {max(box_height) - min(box_height)}')
