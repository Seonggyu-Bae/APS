# 인덱스 이용을 이용하여(효율적으로) merge_sort 작성
def merge_sort(arr,s,e,idx):
    global count
    start, end = s, e
    mid = (start + end) // 2
    if start == end:    # 요소가 하나라면 == 정렬할 필요없음
        return
    # 절반을 각각 정렬한 상태여야 한다.

    merge_sort(arr,s,mid,idx+1)
    merge_sort(arr,mid+1,e,idx+1)

    if arr[mid-1] > arr[end] and idx!= 0:
        count += 1
    # (start ~ mid) (mid+1 ~ end)
    i = start
    j = mid + 1
    tmp = []
    while i<=mid and j<=end:
        # i가 가르키는 값과 j가 가르키는 값 중 더 작은 애를 복사하고
        # i 또는 j를 증가 시키기
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    # 남은거
    while i <= mid:
        tmp.append(arr[i])
        i +=1
    while j <= end:
        tmp.append(arr[j])
        j += 1

    j = 0
    for i in range(start, end+1):
        arr[i] = tmp[j]
        j += 1



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    count = 0

    merge_sort(A,0,N-1,0)
    print(f'#{tc} {A[N//2]} {count}')