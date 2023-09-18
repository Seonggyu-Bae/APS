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
def partition1(arr, l, r):
    p = arr[l]
    i = l
    j = r
    while i<=j:
        while i<=j and A[i] <= p:
            i+=1
        while i<=j and A[i] <= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]

# lomuto
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



T = int(input())

for tc in range(1,T+1):
    N = int(input())
    A = list(map(int, input().split()))

    qsort(A,0,N-1)
    print(f'#{tc} {A[N//2]}')
