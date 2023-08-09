class MyStack:
    def __init__(self, max_size):
        # max_size : 최대 개수
        self.max_size = max_size
        self.s = [None] * max_size
        self.top = -1   # 요소가 들어가거나 뺄 위치를 알려주는 변수
                        # (현재 스택에 들어있는 마지막 요소의 위치를 알려주는 변수)

    def push(self,data):
        # 요소를 스택에 삽입
        if self.top == self.max_size - 1:
            pass
        self.top += 1
        self.s[self.top] = data

    def pop(self):
        # 스택에 들어있는 마지막 요소를 삭제하고 반환
        result = self.s[self.top]
        self.top -= 1
        return result

    # 스택이 비어있으면 True 아니면 False
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    # 스택이 꽉차있으면 True 아니면 False
    def isFull(self):
        if self.top == self.max_size-1:
            return True
        else:
            return False

# 스택의 top 부분을 return 하는 함수 비어있으면 None 반환
    def peek(self):
        if not self.isEmpty():
            return self.s[self.top]
        else:
            return None





stack = MyStack(10)
for i in range(1,11):
    stack.push(i)

for _ in range(10):
    print(stack.pop())