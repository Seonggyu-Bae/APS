from collections import deque


def solve():
    global chk
    my_stack = deque()

    while numtag:
        if chk == numtag[0]:
            numtag.popleft()
            chk += 1
        elif my_stack and my_stack[-1] == chk:
            my_stack.pop()
            chk += 1
        else:
            if numtag and my_stack and numtag[0] < my_stack[-1]:
                my_stack.append(numtag.popleft())
            elif numtag:
                my_stack.append(numtag.popleft())
            else:
                return False
    if my_stack:
        for i in range(len(my_stack)-1,-1,-1):
            if my_stack[i] != chk:
                return False
            else:
                chk +=1

    return True


N = int(input())
numtag = deque(map(int, input().split()))

chk = 1

if solve():
    print('Nice')
else:
    print('Sad')
