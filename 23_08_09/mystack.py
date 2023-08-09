def pop(stack):
    global top

    if top == -1:
        print('underflow!')
        return 0
    else:
        top -= 1
        return stack[top+1]


def push(item,stack):
    global top
    top += 1
    if top==len(stack):
        print('overflow!')
    else:
        stack[top] = item


top  = -1
my_stack = [0] * 10

push(100,my_stack)

print(my_stack)
print(pop(my_stack))