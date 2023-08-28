# 23/08/23

## SW문제해결응용



## 학습목표

- ### SW 문제 해결 역량이란 무엇인가를 이해하고, 역량을 강화하는 방법을 이해한다.

- ### 효율적인 알고리즘의 필요성을 이해하고 알고리즘의 성능 측정 방법 중 하나인 시간복잡도에 대해 이해한다.

- ### 프로그램을 작성하기 위한 기본 중 표준 입출력 방법에 대해 이해한다.

- ### 비트 수준의 연산과 알고리즘에 대해 이해한다.

- ### 컴퓨터에서의 실수 표현 방법에 대해 이해한다.

--- 



## SW 문제 해결



- ### SW 문제 해결 역량이란 무엇인가?
  
  - #### 프로그램을 하기 위한 많은 제약 조건과 요구사항을 이해하고 최선의 방법을 찾아내는 능력
  
  - #### 프로그래머가 사용하는 언어나 라이브러리, 자료구조, 알고리즘에 대한 지식을 적재적소에 퍼즐을 배치하듯 이들을 연결하여 큰 그림을 만드는 능력이라 할 수 있다.
  
  - #### 문제 해결 역량은 추상적인 기술이다.
    
    - ##### 프로그래밍 언어, 알고리즘처럼 명확히 정의된 실체가 없다.
    
    - ##### 무작정 알고리즘을 암기하고 문제를 풀어본다고 향상되지 않는다.
  
  - #### 문제 해결 역량을 향상시키기 위해서 훈련이 필요하다.



- ### 문제 해결 능력을 훈련하기 위해서는
  
  - ##### 일부 새로운 언어, 프레임워크, 개발 방법론만을 배워나가는 것만으로 충분하지 않다. 이들을 조합해 나가는 방법을 배워야 하지만 쉽지 않다.
  
  - ##### 상황을 인위적으로 만들어 훈련해야한다. 즉, 잘 정제된 추상적인 문제를 제시하고 이를 해결해 가면서 문제 해결 능력을 향상 시킬 수 있는 훈련이 필요하다.



- ## 문제 해결 과정

### 1. 문제를 읽고 이해한다.

### 2. 문제를 익숙한 용어로 재정의 한다.

### 3. 어떻게 해결할지 계획을 세운다.

### 4. 계획을 검증한다.

### 5. 프로그램으로 구현한다.

### 6. 어떻게 풀었는지 돌아보고, 개선할 방법이 있는지 찾아본다.



- ## 문제 해결 전략
  
  - ### 직관과 체계적인 접근



- ## 체계적인 접근을 위한 질문들
  
  - ### 비슷한 문제를 풀어본 적이 있던가?
  
  - ### 단순한 방법에서 시작할 수 있을까?
  
  - ### 문제를 단순화 할 수 있을까?
  
  - ### 그림으로 그려 볼 수 있을까?
  
  - ### 수식으로 표현 할 수 있을까?
  
  - ### 문제를 분해 할 수 있을까?
  
  - ### 뒤에서부터 생각해서 문제를 풀 수 있을까?
  
  - ### 특정 형태의 답만을 고려할 수 있을까?

---



## 복잡도 분석



- ### 알고리즘이란?
  
  - #### 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법이다.



- ### 알고리즘의 효율
  
  - #### 공간적 효율성과 시간적 효율성
    
    - ##### 공간적 효율성은 연산량 대비 얼마나 적은 메모리 공간을 요하는 가를 말한다.
    
    - ##### 시간적 효율성은 연산량 대비 얼마나 적은 시간을 요하는 가를 말한다.
    
    - ##### 효율성을 뒤집어 표현하면 복잡도(Complexity)가 된다. 복잡도가 높을수록 효율성은 저하된다.
  
  - #### 시간적 복잡도 분석
    
    - ##### 하드웨어 환경에 따라 처리시간이 달라진다.
    
    - ##### 소프트웨어 환경에 따라 처리시간이 달라진다.



- ### 복잡도의 점근적 표기
  
  - #### 시간 (또는 공간) 복잡도는 입력 크기에 대한 함수로 표기하는데, 이 함수는 주로 여러개의 항을 가지는 다항식이다.
  
  - #### 이를 단순한 함수로 표현하기 위해 점근적 표기(Asymptotic Notation)를 사용한다.
  
  - #### 입력 크기 n이 무한대로 커질 때의 복잡도를 간단히 표현하기 위해 사용하는 표기법이다.
    
    - O(Big-Oh)
    
    - Ω(Big-Omega)
    
    - Θ(Big-Theta)



- #### O(Big-Oh) 표기
  
  - ##### 복잡도의 점근적 상항을 나타낸다.
  
  - ##### 복잡도가 f(n) = 2n^2 - 7n + 4 라면, f(n)의 O-표기는 O(n^2)이다.
  
  - ##### 먼저 f(n)의 단순화된 표현은 n^2이다.
  
  - ##### 단순화된 함수 n^2에 임의의 상수 c를 곱한 cn^2이 n이 증가함에 따라 f(n)의 상한이 된다. (단, c>0)



    













## 표준 입출력 방법

- ### Python3 표준 입출력
  
  - #### 입력
    
    - ##### Raw 값의 입력 :input()
      
      - ###### 받은 입력값을 문자열로 취급
    
    - ##### Evaluated된 값 입력 : eval(input())
      
      - ###### 받은 입력값을 평가된 데이터 형으로 취급
  
  - #### 출력
    
    - ##### print()
      
      - ###### 표준 출력 함수. 출력값의 마지막에 개행 문자가 포함되어있음
    
    - ##### print('text', end = '')
      
      - 출력 시 마지막에 개행문자 제외할 시
    
    - ##### print('%d' %number)
      
      - Formatting 된 출력



- ### 파일의 내용을 표준 입력으로 읽어오는 방법
  
  - #### import sys
  
  - #### sys.stdin = open("a.txt", "r")







## 비트 연산



- ### 비트 연산자
  
  | 연산자 | 연산자의 기능                                            |
  |:---:|:--------------------------------------------------:|
  | &   | 비트 단위로 AND 연산을 한다.<br/>예) num1 & num2              |
  | |   | 비트 단위로 OR 연산을 한다.<br/>예) num1\|num2                |
  | ^   | 비트단위로 XOR 연산을 한다. (같으면 0 다르면 1)<br/>예) num1 ^ num2 |
  | ~   | 단항 연산자로서 피연산자의 모든 비트를 반전시킨다.<br/>예) ~num           |
  | <<  | 피연산자의 비트 열을 왼쪽으로 이동시킨다.<br/>예)num << 2             |
  | >>  | 피연산자의 비트 열을 오른쪽으로 이동시킨다.<br/>예) num >> 2           |



