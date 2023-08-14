def forth(expression):
    my_stack = []
    for i in range(len(expression)):

        if expression[i] not in '(+-*/.)':
            my_stack.append(int(expression[i]))

        elif expression[i] == '.':
            if len(my_stack)>1:
                return 'error'
            return my_stack[0]

        elif expression[i] == '+':
            if len(my_stack) >= 2:
                a = my_stack.pop()
                b = my_stack.pop()
                temp = int(b) + int(a)
                my_stack.append(temp)
            else:
                return 'error'

        elif expression[i] == '-':
            if len(my_stack) >= 2:
                a = my_stack.pop()
                b = my_stack.pop()
                temp = int(b) - int(a)
                my_stack.append(temp)
            else:
                return 'error'

        elif expression[i] == '*':
            if len(my_stack) >= 2:
                a = my_stack.pop()
                b = my_stack.pop()
                temp = int(b) * int(a)
                my_stack.append(temp)
            else:
                return 'error'

        elif expression[i] == '/':
            if len(my_stack) >= 2:
                a = my_stack.pop()
                b = my_stack.pop()
                temp = int(b) // int(a)
                my_stack.append(temp)
            else:
                return 'error'


T = int(input())

for tc in range(1, T + 1):
    expression = list(input().split())

    print(f'#{tc} {forth(expression)}')
