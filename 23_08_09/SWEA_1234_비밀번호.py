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


# 0~9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍들을 소거하고 남은 번호를 비밀번호로 만드는 것입니다.
# 번호 쌍이 소거되고 소거된 번호 쌍의 좌우 번호가 같은 번호이면 또 소거 할 수 있습니다.

for tc in range(1, 11):
    # 숫자열의 길이, 숫자열
    pass_len, i_str = list(input().split())

    # 스택 생성
    cs_password = MyStack(len(i_str))
    # 입력받은 숫자열의 첫번째를 push
    cs_password.push(i_str[0])


    # push 하고 그 앞의 번호와 비교해서 같으면 pop 2번하면 top = top-2 가 된다
    for i in range(1,len(i_str)):
        cs_password.push(i_str[i])
        if cs_password.s[cs_password.top-1] == cs_password.s[cs_password.top]:
            cs_password.pop()
            cs_password.pop()

    # 다 끝내고 나서 0부터 top+1까지가 알아낸 비밀번호임
    ans = ''.join(cs_password.s[0:cs_password.top+1])
    print(f'#{tc} {ans}')