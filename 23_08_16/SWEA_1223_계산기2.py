"""
문자열 계산식을 구성하는 연산자는 +, * 두종류이며
피연산자인 숫자는 0 ~ 9의 정수만 주어진다

중위 -> 후위
피연산자면 출력
연산자라면
stack[top]에 저장되어있는 연산자보다 높으면 스택에 push
아니면 스택[top]의 연산자의 우선순위가 작을때까지 스택에서 pop하고 push
top에 연산자가 없으면 push

"""


def postfix(exp):
    post = ''
    stack = []
    for c in exp:
        if c in '+*':
            if not stack:
                stack.append(c)
            else:
                if c == '+':
                    if not stack:
                        stack.append(c)
                    else:
                        while stack:
                            post += stack.pop()
                        stack.append(c)
                else:
                    while priority[stack[-1]] > priority[c] or not stack:
                        post += stack.pop()
                    stack.append(c)
        else:
            post += c
    while stack:
        post += stack.pop()
    return post


def forth(exp):
    stack = []

    for c in exp:
        if c in '+*':
            a = stack.pop()
            b = stack.pop()
            if c == '+':
                temp = int(a) + int(b)
            else:
                temp = int(a) * int(b)
            stack.append(temp)
        else:
            stack.append(c)

    return stack[0]


for tc in range(1, 11):
    s_len = int(input())
    expression = list(input())
    priority = {'+': 0, '*': 1}
    #print(postfix(expression))
    print(f'#{tc} {forth(postfix(expression))}')
