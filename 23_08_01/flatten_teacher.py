def find_min_max(boxes):
    max_idx = 0
    min_idx = 0
    for i in range(100):
        if boxes[i] > boxes[max_idx]:
            max_idx = i
        if boxes[i] < boxes[min_idx]:
            min_idx = i

    return max_idx,min_idx


T = 10

for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))
    for _ in range(N):
        max_idx, min_idx = find_min_max(boxes)
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    max_idx, min_idx = find_min_max(boxes)
    print(f'#{tc} {boxes[max_idx] - boxes[min_idx]}')