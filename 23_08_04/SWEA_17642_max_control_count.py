T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())
    
    # 예외처리를 잘 하자
    if A > B:
        print(f'#{tc} -1')
        continue
    elif A == B:
        print(f'#{tc} 0')
        continue

    diff = B-A
    count = 0

    if diff % 2 == 0:
        count = diff // 2
    elif (diff-3) % 2 == 0:
        count = ((diff-3) // 2) + 1

    if count:
        print(f'#{tc} {count}')
    else:
        print(f'#{tc} -1')

