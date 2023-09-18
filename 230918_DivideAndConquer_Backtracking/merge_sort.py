# 정렬된 두개의 배열을 합치는 것이 핵심
# 시간복잡도 생각하지않고 간단하게 개념 이해를 위한 코드임
def merge_sort(arr):    # 정렬된 배열을 반환하는 것이 목표
    # [1, 3, 7, 10, 4, 5, 6, 8]
    if len(arr) == 1: # 요소가 하나니까 정렬된것임
        return arr
    mid = len(arr)//2

    arr1 = merge_sort(arr[:mid])    # 정렬되어 있는 배열이라고 생각
    arr2 = merge_sort(arr[mid:])

    new_arr = []
    # arr1 과 arr2의 가장 앞 요소를 비교해서 작은것 pop하고
    # new_arr에 append

    while arr1 and arr2:    # 둘 다 요소를 가지고 있을때 까지만
        if arr1[0] < arr2[0]:
            new_arr.append(arr1.pop(0))
        else:
            new_arr.append(arr2.pop(0))
    # arr1 또는 arr2 둘 중에 하나만 비어 있는 상태임
    new_arr += arr1
    new_arr += arr2

    return new_arr


print(merge_sort([2, 414, 51, 3, 13, 4, 23, 124, 15, 62, 16]))