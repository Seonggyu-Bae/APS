def merge_sort(arr):
    global count

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    if left[-1] > right[-1]:
        count += 1
    l_len = len(left)
    r_len = len(right)

    idx, l_idx, r_idx = 0, 0, 0

    while l_idx < l_len and r_idx < r_len:
        if left[l_idx] <= right[r_idx]:
            arr[idx] = left[l_idx]
            l_idx += 1
        else:
            arr[idx] = right[r_idx]
            r_idx += 1
        idx += 1

    # 남은거
    while l_idx < l_len:
        arr[idx] = left[l_idx]
        idx += 1
        l_idx += 1
    while r_idx < r_len:
        arr[idx] = right[r_idx]
        idx += 1
        r_idx += 1

    return arr


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    count = 0

    merge_sort(A)
    print(f'#{tc} {A[N // 2]} {count}')
