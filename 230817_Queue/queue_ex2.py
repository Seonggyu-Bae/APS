# 선형 Queue
class MyQ:
    def __init__(self, N):
        self.Q = [None] * N
        self.front = self.rear = -1

    # queue 에 데이터 삽입
    def enQ(self, data):
        if self.isFull():
            print("큐가 가득 차 있습니다.")
        else:
            self.rear += 1
            self.Q[self.rear] = data

    # queue 에 가장 먼저 들어온 요소를 삭제(선형큐에서는 인덱스가 다시 뒤로 가진 않아서) 및 반환
    def deQ(self):
        if self.isEmpty():
            print("큐가 비어있습니다.")
        else:
            self.front += 1
            return self.Q[self.front]

    # 큐가 가득 찼는지 검사
    def isFull(self):
        return self.rear == len(self.Q)-1

    # 큐가 비어있는지 검사
    def isEmpty(self):
        return self.front == self.rear




Q = MyQ(5)

Q.enQ(1)
Q.enQ(2)
Q.enQ(3)
Q.enQ(4)
Q.enQ(5)
Q.deQ()
Q.deQ()
Q.deQ()
Q.deQ()
Q.deQ()
Q.deQ()
Q.enQ(1)    #  선형 큐의 단점 공간이 비어있음에도 불구하고 더 넣을 수없다



