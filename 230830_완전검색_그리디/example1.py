def selection_sort(arr, start, end):
    if start == end:
        return 0
    else:
        minI = start
        for i in range(start + 1, end):
            if arr[minI] > arr[i]:
                minI = i
        arr[i], arr[minI] = arr[minI], arr[i]
        selection_sort(arr,start+1,end)



A = [124, 31, 513, 3564, 64, 2343, 35, 2, 13213, 12]

print(selection_sort(A, 0, 10))
