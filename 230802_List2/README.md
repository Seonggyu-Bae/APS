# 23/08/02

##### 2차원 배열

- 1차원 List를 묶어놓은 List

- 2차원 이상의 다차원 List는 차원에 따라 Index를 선언

- 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함

- Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

- arr = [[0,1,2,3],[4,5,6,7]] (2행 4열의 2차원 List)

##### 배열 순회

- N X M 배열의 N*M 개의 모든 원소를 빠짐없이 조사하는 방법
  
  **행 우선순회**

- ```python
  for i in range(n):
      for j in range(m):
          Array[i][j]
  ```

**열 우선순회**

- ```python
  for j in range(m):
      for i in range(n):
          Array[i][j]
  ```

**지그재그 순회**

- ```python
  for i in range(n):
      for j in range(m):
          Array[i][j + (m-1-2*j) * (i%2)]
  ```

#### 델타를 이용한 2차 배열 탐색

- **2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법**

- ```python
  arr[][] #NXM
  
  di = [0, 1, 0, -1]
  dj = [1, 0, -1, 0]
  
  for i in range(N):
      for j in range(M):
          for k in range(4):
              ni = i + di[k]
              nj = j + dj[k]
              if 0 <= ni <= N and 0 <= nj <= N #is valid index?
                  Array[ni][nj]
  ```

```python
#전치행렬

arr = [[1,2,3], [4,5,6], [7,8,9]]
"""
123
456
789
"""

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr) # [[1,4,7], [2,5,8], [3,6,9]
"""
147
258
369
"""
```

##### 검색(Search)

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업

- 목적하는 탐색 키를 가진 항목을 찾는 것
  
  - 탐색 키( Search Key) : 자료를 구별하여 인식할 수 있는 키

- 검색의 종류
  
  - 순차 검색(Sequential Searach)
  
  - 이진 검색(Binary Search)
  
  - 해쉬 (Hash)

**순차 검색(Sequential Search)**

- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
  
  - 가장 간단하고 직관적인 검색 방법
  
  - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
  
  - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임

- 2가지 경우
  
  - 정렬되어 있지 않은 경우
    
    - 첫번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다.
    
    - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
    
    - 자료구조의 마지막에 이를 때 까지 검색 대상을 찾지 못하면 검색 실패
    
    - 찾고자 하는 원소의 순서에 따라 비교 회수가 결정됨
      
      - 첫번째 원소를 찾을 때는 1번 비교, 두번째 원소를 찾을 때는 2번 비교
    
    - 정렬되지 않은 자료에서의 순차 검색의 평균 비교 회수 = (1/n) * (1+2+3+ ... + n) = (n+1)/2
    
    - 시간 복잡도 : O(N)
  
  ```python
  def seqserch(a, n, key):
      i = 0
      while i<n and a[i]!= key:
          i = i+1
      if i<n:
          return i
      else:
          return -1
  ```
  
  - 정렬되어 있는 경우
    
    - 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정
    
    - 자료를 순차적으로 검색하면서 키 값을 비료하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색종료
    
    - 찾고자 하는 원소의 순서에 따라 비교회수가 결정
      
      - 정렬이 되어있으므로, 검색 실패를 반환하는 경우 평균 비교회수가 반으로 줄어듬
      
      - 시간 복잡도 : O(N)
  
  ```python
  def seqserch2(a, n, key):
      i = 0
      while i < n and a[i] < key:
          i = i+1
      if i < n and a[i] == key:
          return i
      else:
          return -1
  ```

 

##### 이진 검색(Binary Search)

- 검색과정
  
  - 자료의 중앙에 있는 원소를 고른다.
  
  - 중앙 원소의 값과 찾고자 하는 목표 값을 비교
  
  - 목표 값이 중앙값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색 수행, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행
  
  - 찾고자 하는 값을 찾을 때 까지 위 과정을 반복

- 구현
  
  - 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행
  
  - 이진 검색의 경우, 자료에 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬 상태로 유지하는 추가 작업 필요

- ```python
  def binsearch(a, N, key):
      start = 0
      end = N-1
      while start <= end:
          middle = (start + end) //2
          if a[middle] == key:        # search !
              return true
          elif a[middle] > key:
              end = middle -1
          else:
              start = middle + 1
      return false                # search fail
  ```

```python
def binsearch2(a, low, high, key):
    if low > high: # search fail
        return false
    else:
        middle = (low + high) //2
        if key == a[middle]:        # search !
            return true
        elif key < a[middle]:
            return binsearch2(a, low, middle-1, key)
        elif key > a[middle]:
            return binsearch2(a, middle+1, high, key)
```
