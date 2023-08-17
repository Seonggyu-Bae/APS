
def makeback(fx):
    stack = [0] * len(fx)
    top = -1
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}      # 스택으로 들어갈때 우선순위 숫자가 높을수록 높음
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}      # 스택에서 나올때(스택안에서) 우선순위 숫자가 높을수록 높음

    for x in fx:
        if x in '(+-*/)':
            if top == -1 or isp[stack[top]] < icp[x]: # 토큰의 우선순위가 더 높으면
                top += 1 # push
                stack[top] = x




expression = '6528-*2/+'

for x in expression:
    if x not in '+-/*':  # 피연산자라면
        top += 1  # push
        stack[top] = int(x)

    else:
        if x == '+':
            op1 = stack[top]  # pop
            top -= 1
            op2 = stack[top]
            top -= 1
            # 연산순서 확실히
            stack[top] = op1 + op2
            top += 1

        elif x == '-':
            op1 = stack[top]  # pop
            top -= 1
            op2 = stack[top]
            top -= 1
            # 연산순서 확실히
            stack[top] = op2 - op1
            top += 1

        elif x == '/':
            op1 = stack[top]  # pop
            top -= 1
            op2 = stack[top]
            top -= 1
            # 연산순서 확실히
            stack[top] = op2 / op1
            top += 1

        elif x == '*':
            op1 = stack[top]  # pop
            top -= 1
            op2 = stack[top]
            top -= 1
            # 연산순서 확실히
            stack[top] = op2 * op1
            top += 1

print(stack[-1])
