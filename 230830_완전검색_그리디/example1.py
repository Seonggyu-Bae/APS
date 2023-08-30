def selection_sort(arr, start, end):
    if start == end - 1:
        return
    else:
        minI = start
        for i in range(start + 1, end):
            if arr[minI] > arr[i]:
                minI = i
        arr[start], arr[minI] = arr[minI], arr[start]
        print(arr)
        selection_sort(arr, start + 1, end)


A = [124, 31, 513, 3564, 64, 2343, 35, 2, 13213, 12]
print(A)
selection_sort(A, 0, 10)
