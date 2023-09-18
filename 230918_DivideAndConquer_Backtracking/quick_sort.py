def quick_sort(arr):
    # 요소가 1개이거나 없을 경우
    if len(arr) <= 1:
        return arr
    # 임의로 arr의 요소 하나(P : pivot)를 선정
    P = arr.pop()
    # P를 기준으로 작은것과 큰것들을 모아서
    # 작은것은 P 앞쪽에
    left = [e for e in arr if e < P]
    # 큰거는 P 뒤쪽에
    right = [e for e in arr if e >= P]
    
    left = quick_sort(left)
    right = quick_sort(right)

    return left + [P] + right



print(quick_sort([4, 7, 1, 5, 9, 3, 6, 8, 2]))