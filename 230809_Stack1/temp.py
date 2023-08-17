def pop(my_stack):
    global top
    if top == -1:
        return None
    else:
        top -= 1
        return my_stack[top + 1]


def push(my_stack,item):
    global top
    top += 1
    if top == len(my_stack):
        return None
    else:
        my_stack[top] = item

    return 0

def isEmpty():
    global top

    if top == -1:
        return True
    else:
        return False

def two_bracket_search(search_txt):
    a,b,c,d = 0,0,0,0
    global top
    tex_len = len(search_txt)

    for i in range(tex_len):
        if search_txt[i] == '{':
            a += 1
        elif search_txt[i] == '}':
            b += 1
        elif search_txt[i] == '(':
            c += 1
        elif search_txt[i] == ')':
            d += 1
    if a!=b or c!=d:
        return 0

    check_lst = [None] * tex_len

    for i in range(tex_len):
        if search_txt[i] == '{':
            push(check_lst,'{')
        elif search_txt[i] == '}':
            if pop(check_lst) != '{':
                return 0

        elif search_txt[i] == '(':
            push(check_lst, '(')
        elif search_txt[i] == ')':
            if pop(check_lst) != '(':
                return 0

    if isEmpty():
        return 1
    else:
        return 0


T= int(input())

for tc in range(1,T+1):

    my_list = list(input())
    top = -1
    print(f'#{tc} {two_bracket_search(my_list)}')
