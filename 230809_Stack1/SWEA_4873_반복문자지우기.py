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

    def peek(self):
        if not self.isEmpty():
            return self.s[self.top]
        else:
            return None

T = int(input())

for tc in range(1, T+1):
    i_str = list(input())

    good = MyStack(len(i_str))
    good.push(i_str[0])

    for i in range(1,len(i_str)):
        good.push(i_str[i])
        if good.s[good.top-1] == good.s[good.top]:
            good.pop()
            good.pop()

    print(f'#{tc} {good.top+1}')