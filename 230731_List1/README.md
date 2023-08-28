# 23/07/31

APS(Algorithm Problem Solving)

##### APS 과정의 목표 중의 하나는 보다 좋은 알고리즘을 이해하고 활용하는 것이다.

###### 무엇이 좋은 알고리즘인가?

1. 정확성 :  얼마나 정확하게 동작하는가

2. 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가

3. 메모리 사용량 : 얼마나 적은 메모리를 사용하는가

4. 단순성 : 얼마나 단순한가

5. 최적성 : 더 이상 개선할 여지 없이 최적화되었는가

###### 알고리즘의 작업량을 표현할 때 시간복잡도로 표현한다.

###### 시간 복잡도(Time Complexity)

- 실제 걸리는 시간을 측정

- 실행되는 명령문의 개수를 계산

###### 배열이란?

- 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

###### 배열의 필요성

- 프로그램 내에서 여러 개의 변수가 필요할 때, 일일이 다른 변수명을 이용하여 자료에 접근하는 것은 매우 비효율적일 수 있다.

- 배열을 사용하면 하나의 선언을 통해서 둘 이상의 변수를 선언할 수 있다.

- 단순히 다수의 변수 선언을 의미하는 것이 아니라, 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있다.

###### 정렬

- 2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값(오름차순 :  ascending), 혹은 그 반대의 순서대로 (내림차순 : descending)  재배열하는 것

- 키
  
  - 자료를 정렬하는 기준이 되는 특정 값

###### 버블 정렬(Bubble Sort)

- 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

- 정렬과정
  
  - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.
  
  - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
  
  - 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블 정렬이라고 한다.

- 시간 복잡도 O(n^2)