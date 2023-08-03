def selectionsort(a, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

    return a

def commonselectionalgorithm(arr,k):
    for i in range(k):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx], arr[i]
    return arr[k-1]



my_list = [21421, 5, 1, 2, 3, 4, 214, 53256, 324, 123, 4, 245, 35, 344, 3242, 432, 6423, 6, 24]

print(selectionsort(my_list,len(my_list)))
print(commonselectionalgorithm(my_list,8))

