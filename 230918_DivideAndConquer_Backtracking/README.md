# 23/09/18



## 학습 목표

- 문제를 분할해서 해결하는 분할 정복(Divide and Conquer) 기법을 이해하고 대표적인 알고리즘인 퀵 정렬과 병합 정렬에 대해 학습한다.

- 상태 공간 트리의 모든 노드를 검색하는 백트래킹에 대해 학습한다.

- 이진 트리(Binary Tree)의 특성을 이해하고 이진 트리의 중요한 연산인 탐색, 삽입, 삭제 알고리즘을 학습한다.



## 분할 정복 기법



**설계 전략**

- 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다.

- 정복(Conquer) : 나눈 작은 문제를 각각 해결한다.

- 통합(Combine) : (필요하다면) 해결된 해답을 모은다.



**Top-down approach**



**병합 정렬(Merge Sort)**

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식

- 분할 정복 알고리즘 활용
  
  - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
  
  - top-down 방식

- 시간 복잡도
  
  - O(n log n)

- **분할과정**
  
  ```python
  merge_sort(LIST m):
      if length(m) == 1:
          return m
      LIST left, right
      middle = length(m) / 2
      for x in range(middle):
          left.append(m[x])
      for x in range(middle,length(m)):
          right.append(m[x])
      left = merge_sort(left)
      right = merge_sort(right)
      
      return merge(left, right)
  ```

- **병합과정**
  
  ```python
  merge(LIST left, LIST right):
      LIST result
  
      while length(left) > 0 or length(right) > 0:
          if length(left) > 0 and length(right) > 0:
              if first(left) <= first(right):
                  result.append(left.pop(0))
              else:
                  result.append(right.pop(0))
          elif length(left) > 0:
              result.append(left.pop(0))
          elif length(right) > 0:
              result.append(right.pop(0))
      return result
  ```



**퀵 정렬**

- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.
  
  - 병합 정렬과 동일한가?

- 다른점 1 :  병합 정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 때, 기준 아이템(pivot item) 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.

- 다른점 2 : 각 부분 정렬이  끝난 후, 병합정렬은 "병합"이란 후처리 작업이 필요하지만 퀵정렬은 필요하지 않다.

- **알고리즘**
  
  ```python
  qsort(A[], L, r):
      if L < r
          s = partition(a,L,r)
          qsort(A[], L, s-1)
          qsort(A[], s+1, r)
  
  ```
  
  ```python
  partition(A[], L, r):        # Hoare-Partition
      p = A[L]    //p : 피봇 값
      i = L
      j = r
      while i <= j:
          while i <= j and A[i] <= p:
              i += 1
          while i <= j and A[j] >= p:
              j -= 1
          if i < j:
              A[i], A[j] = A[j], A[i]
  
  
      A[L],A[j] = A[j], A[L]
      return j
  ```



**이진검색**

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
  
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함

- **이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.**

- **검색과정**
  
  1. 자료의 중앙에 있는 원소를 고른다.
  
  2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
  
  3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
  
  4. 찾고자 하는 값을 찾을 때까지 1~3의 과정을 반복한다.

- 참고 : 이진탐색 공부 후 Parametric Search 공부하기


