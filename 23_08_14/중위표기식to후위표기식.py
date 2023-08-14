# 중위표기식을 후위표기식으로 바꿀것
# 연산 우선순위가 높은 애가 먼저 출력될 수 있도록 해야함
# 정상적인 중위표기식이 들어왔다고 가정하고 작성된 코드


exp = '(6+5*(2-8)/2)'
post_exp = ''
stack = []

# 우선순위를 비교하기 위한 딕셔너리
# 괄호를 처리하기 위해 우선순위를 2가지 만들어야함
# 괄호는 stack 안에 있을때랑 밖에 있을 때 우선순위가 다름
# 스택 안에 있을때는 괄호안에 다른 연산자들이 다 처리하고 괄호가 없어져야하니까 우선순위가 낮다.
# 스택에 들어가야할때는 다른 연산자들 보다 괄호가 먼저 처리되야 함으로 우선순위가 높다.
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}  # in_stack_priority
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}  # in_coming_priority

for c in exp:
    # 하나씩 읽어오기
    # 피연산자인지 연산자인지 확인!
    # 피연산자라면 출력 연산자라면 우선순위에 따라서 스택에 넣거나 출력

    if c in '+-*/()':  # 연산자면

        if c == ')':  # 닫는괄호라면 여는 괄호 만날때까지 전부 pop
            while stack[-1] != '(':
                post_exp += stack.pop()
            stack.pop()         # 여는 괄호는 필요없음
            continue

        # 연산자가 처음들어갈때 (스택이 비어있을때)
        if not stack:
            stack.append(c)
        # stack[top]의 연산자보다 우선순위가 높으면 넣기
        elif isp[stack[-1]] < icp[c]:
            stack.append(c)

        # stack[top]의 연산자보다 우선순위가 같거나 낮으면
        else:
            # 나보다 우선순위가 낮은애가 stack[top]이 될때까지 뻬야함
            while stack and isp[stack[-1]] >= icp[c]:
                post_exp += stack.pop()
            # while문을 통해서 우선순위가 높은애들은 다 빠졌으니 들어갈 수 있음
            stack.append(c)

    else:  # 피연산자
        post_exp += c

while stack:        # 스택에 남아있는 연산자 출력
    post_exp += stack.pop()

print(post_exp)