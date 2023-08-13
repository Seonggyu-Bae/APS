"""
선택정렬(Selection Sort)
주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

정렬과정
1. 주어진 리스트 중에서 최소값을 찾는다.
2. 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위 과정을 반복한다.

시간복잡도
O(N^2)
"""

def selectionsort(a, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        # print(a)
        a[i], a[min_idx] = a[min_idx], a[i]
        # print(a)

    return a

"""
셀렉션 알고리즘(Selection Algorithm)
저장되어 있는 자료로부터 K번째로 큰 또는 작은 원소를 찾는 방법
- 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다.

선택과정
1. 정렬 알고리즘을 이용하여 자료 정렬하기
2. 원하는 순서에 있는 원소 가져오기

K가 비교적 작을 떄 유용하며 O(KN) 의 수행시간을 필요로 한다.
"""


def commonselectionalgorithm(arr,k):
    for i in range(k):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx], arr[i]
    return arr[k-1]



# 선택정렬후
# 8 번째로 작은 원소를 찾음

my_list = [21421, 5, 1, 2, 3, 4, 214, 53256, 324, 123, 4, 245, 35, 344, 3242, 432, 6423, 6, 24]

print(selectionsort(my_list,len(my_list)))
print(commonselectionalgorithm(my_list,8))

