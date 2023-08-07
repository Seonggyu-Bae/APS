import random

my_list = [[0] * 5 for _ in range(5)]
N = int(input())
# my_list = [[0]*5] * 5 로 하면
"""
2차원 리스트의 값을 초기화할 때 리스트 컴프리헨션을 사용하지 않고 
[[0]*5, ]*5와 같이 리스트를 생성하면, 
리스트의 원소가 서로 연결되어 있기 때문에 값이 같아지는 문제가 발생합니다.

표현식 [[0]*5, ]*5에서 다음과 같은 일이 벌어집니다.

[[0]*5]는 [0, 0, 0, 0, 0]을 하나의 리스트로 갖는 2차원 리스트를 만듭니다.
[[0, 0, 0, 0, 0]]*5는 위에서 만든 2차원 리스트를 다시 5번 반복하여 하나의 리스트로 갖는 3차원 리스트를 만듭니다. 하지만 이때 5개의 리스트가 모두 같은 객체를 참조하고 있습니다.

즉, 2차원 리스트의 각 행은 동일한 내부 리스트를 공유하게 됩니다. 
그래서 하나의 행의 값을 변경하면, 다른 행들도 모두 변경되는 결과를 보이게 됩니다.
이러한 문제를 해결하려면 독립적인 내부 리스트를 갖는 리스트를 생성해야 합니다. 
이를 위해서는 리스트 컴프리헨션을 사용하여 각 행을 독립적으로 생성하면 됩니다.
"""
# my_list의 각 항목의 상하좌우 값과의 차이의 절댓값의 합을 구하는 코드

print(my_list)

for i in range(5):
    for j in range(5):
        a = random.randint(1, 100)
        my_list[i][j] = a

my_arr = [list(map(int,input().split())) for _ in range(N)]

print(my_list)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
my_sum = 0

for i in range(5):
    for j in range(5):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5:  # is index valid?
                my_del = my_list[i][j] - my_list[ni][nj]
                if my_del > 0:
                    my_sum += my_del
                else:
                    my_sum += -my_del

print(my_sum)
