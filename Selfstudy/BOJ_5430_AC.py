from collections import deque
from sys import stdin


def solve():
    is_reverse = False
    for f in p:
        if f == 'R':
            if is_reverse:
                is_reverse = False
            else:
                is_reverse = True
        else:
            if num:
                if is_reverse:
                    num.pop()
                else:
                    num.popleft()
            else:
                return False
    if is_reverse:
        num.reverse()
    return True


T = int(stdin.readline().rstrip())

for tc in range(T):
    func = stdin.readline().rstrip()
    n_len = int(stdin.readline().rstrip())
    x = stdin.readline().rstrip()
    num = deque()
    if n_len > 0:
        num = deque(map(int, x[1:-1].split(',')))
    p = ''
    count = 0
    for f in func:
        if f == 'R':
            count += 1
        else:
            if count % 2 == 0:
                p += 'D'
            else:
                p += 'RD'
            count = 0
    if count % 2 != 0:
        p += 'R'

    if solve():
        if num:
            print(f'[{",".join(num)}]')
        else:
            print('[]')
    else:
        print('error')
