from collections import deque
from sys import stdin


def solve():
    # 함수 'R'이 나오면 뒤집어야 하지만
    # 뒤집지 않고 표시만 해둠 -> 연산을 줄여 시간복잡도를 낮춤
    # 'D'가 나오면 뒤집혀있으면 맨 뒷쪽 숫자를 지우고
    # 정방향이라면 맨 앞쪽 숫자를 지우면된다
    is_reverse = False
    for f in func:
        if f == 'R':
            is_reverse = not is_reverse
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

    if n_len:
        # 슬라이싱과 split을 이용해서 함수 사용을 쉽게 만들어줌
        x = x[1:-1].split(',')
    else:
        x = []

    num = deque(x)

    if solve():
        if num:
            print(f"[{','.join(list(num))}]")
        else:
            print('[]')
    else:
        print('error')
