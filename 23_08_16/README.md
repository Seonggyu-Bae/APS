# 23/08/16



#### 부분 집합의 합

- 집합 {1, 2, 3}의 원소에 대해 각 부분집합에서의 포함 여부를 트리로 표현











### 분할 정복 알고리즘



##### 설계 전략

- 분할(Divide) :  해결할 문제를 여러 개의 작은 부분으로 나눈다.

- 정복(Conquer) : 나눈 작은 문제를 각각 해결한다.

- 통합(Combine) : (필요하다면) 해결된 해답을 모은다.



###### 예제

- 거듭 제곱(Exponentiation)

- ```python
  def Power(Base, Exponent):
      if Base == 0:
          return 1
  
      result = 1 # Base^0는 1이므로
      for i in range(Exponent):
          result *= Base
  
      return result
  ```





- 분할 정복 기반 O(logN)

- C^n = C^(n/2) *  C^(n/2) -> n은 짝수

- C^n = C^(n-1)/2 * C^(n-1)/2 * C -> n은 홀수

- ```python
  def Power(Base, Exponent) : 
      if Exponent == 0 or Base == 0:
          return 1
      
      if Exponent % 2 == 0:
          NewBase = Power(Base, Exponent/2)
          return NewBase * NewBase
      
      else:
          NewBase = Power(Base, (Exponent-1)/2)
          return (NewBase * NewBase) * Base
  ```



### 퀵 정렬 (나중에 자세히 다룬다)

- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다. (합병정렬과 동일한가?)

##### 다른점

1. 합병정렬은 그냥 두 부분으로 나누는 반면에, 퀵정렬은 분할할 때, 기준 아이템(pivot) 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.

2. 각 부분 정렬이 끝난 후, 합병정렬은 "합병" 이란 후처리 작업이 필요하나, 퀵정렬은 필요하지 않는다.
