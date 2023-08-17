T = int(input())

for tc in range(1, T+1):

    info = list(input())

    count = 0
    ans = 0

    for i in range(len(info)):
        if info[i] == '(':
            count += 1

        else:
            if info[i-1] == '(':
                count -= 1
                ans += count

            else:
                count -= 1
                ans += 1

    print(f'#{tc} {ans}')