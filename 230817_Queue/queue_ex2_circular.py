class MyQ2:
    def __init__(self,N):
        self.Q = [None] * N
        self.front = self.rear = 0

    def enQ(self,data):
        # rear를 1 증가하고 그 위치에 데이터 삽입
        if not self.isFull():
            self.rear = (self.rear + 1) % len(self.Q)
            self.Q[self.rear] = data
        else:
            print('가득참')

    def deQ(self):
        if not self.isEmpty():
            self.front = (self.front+1) % len(self.Q)
            return self.Q[self.front]
        else:
            print('없음')

    def isFull(self):
        # rear의 다음칸이 front라면 가득참
        # front와  rear가 같은 칸에 있으면 비어있다고 판단할것임
        # front의 위치에 데이터를 삽입하면 안된다.
        if (self.rear + 1) % len(self.Q) == self.front:
            return True
        return False

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False