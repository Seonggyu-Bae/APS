# 1. 파티셔닝
# 2. 퀵소트

def qsort(arr,l,r):
    # 그림을 그리면 종료조건도 쉽게 찾을 수 있다.
    if l >= r:
        return

    # Pivot 기준으로 작은값/큰값 나누어주기 (partition)
    # 다시 left, right 각각 퀵정렬

    p = partition2(arr,l,r)
    # p : 피벗 위치
    qsort(arr,l,p-1)
    qsort(arr,p+1,r)

    return arr


# hoare
# l, r 기준(범위), pivot 잡고 작은값 큰 값 나누어주기
# pivot 위치 반환
def partition1(arr,l,r):
    # 가장 앞 요소를 pivot으로 잡고
    pivot = arr[l]
    # 초기값 : 가장 왼쪽 요소를 가르키는 i, 가장 오른쪽 요소를 가르키는 j
    i, j = l, r
    # i는 pivot보다 큰 값을 찾으면서 오른쪽으로 이동
    # j는 pivot보다 작은 값을 찾으면서 왼쪽으로 이동
    # 각각 위치를 찾았으면 요소 교환
    # i가 j 위치보다 작을때까지 (왼쪽에 있을때까지) 반복
    while i < j:
        while i<=j and arr[i] <= pivot:
            i += 1
        while i<=j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # 반복이 끝났다면, j가 가르치는 요소와 pivot의 위치 교환
    arr[l], arr[j] = arr[j], arr[l]

    return j


#lomuto
def partition2(arr, l, r):
    # 가장 끝 요소를 pivot으로 잡고
    pivot = arr[r]
    # i : 작은 값이 들어갈 위치
    # j : 작은 값의 위치
    i = l - 1
    # j를 오른쪽으로 이동(증가)시키면서 피벗보다 작은 값을 찾으면 멈추기
    # i와 j의 위치에 있는 요소 교환
    for j in range(l,r):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r], arr[i+1]

    return i+1


arr = [4, 2, 1, 3, 6, 2]
qsort(arr,0,len(arr)-1)
print(arr)
print(qsort(arr,0,len(arr)-1))